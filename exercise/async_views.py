import logging
from django.utils.translation import ugettext_lazy as _

from lib.email_messages import email_course_error
from lib.helpers import extract_form_errors
from notification.models import Notification
from .forms import SubmissionCallbackForm


logger = logging.getLogger('aplus.exercise')


def _post_async_submission(request, exercise, submission, errors=None):
    """
    Creates or grades a submission.

    Required parameters in the request are points, max_points and feedback. If
    errors occur or submissions are no longer accepted, a dictionary with
    "success" is False and "errors" list will be returned.
    """
    if not errors:
        errors = []

    # Use form to parse and validate the request.
    form = SubmissionCallbackForm(request.POST)
    errors.extend(extract_form_errors(form))
    if not form.is_valid():
        submission.feedback = _(
            "<div class=\"alert alert-error\">\n"
            "<p>练习评估服务出现故障. "
            "已通知工作人员.</p>\n"
            "<p>现在，此提交被标记为错误.</p>\n"
            "</div>")
        submission.set_error()
        submission.save()
        if exercise.course_instance.visible_to_students:
            msg = "练习服务返回无效的成绩请求: {}"\
                .format("\n".join(errors))
            logger.error(msg, extra={"request": request})
            email_course_error(request, exercise, msg, False)
        return {
            "success": False,
            "errors": errors
        }

    # Grade the submission.
    try:
        submission.set_points(form.cleaned_data["points"],
                              form.cleaned_data["max_points"])
        submission.feedback = form.cleaned_data["feedback"]
        submission.grading_data = request.POST

        if form.cleaned_data["error"]:
            submission.set_error()
        else:
            submission.set_ready()
        submission.save()

        if form.cleaned_data["notify"]:
            Notification.send(None, submission)
        else:
            Notification.remove(submission)

        return {
            "success": True,
            "errors": []
        }

    # Produce error if something goes wrong during saving the points.
    except Exception as e:
        logger.exception("Unexpected error while saving grade"
            " for {} and submission id {:d}".format(str(exercise), submission.id));
        return {
            "success": False,
            "errors": [repr(e)]
        }
