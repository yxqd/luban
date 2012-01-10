# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban.workflows.feedback import Workflow
import luban
luban.app_config.register(
    'gmail_account',
    "gmail account info",
    "{'username': '...', 'password': '...'}",
    )
luban.app_config.register(
    'feedback_recipient',
    'feedback recipient email address',
    'feedback@mysite.com',
    )

workflow = Workflow()
workflow.actor_factory.feedback_recipient = luban.app_config.feedback_recipient
workflow.actor_factory.gmail_account = luban.app_config.gmail_account

# End of file 