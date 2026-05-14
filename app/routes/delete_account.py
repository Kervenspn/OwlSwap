from flask import Blueprint, redirect, url_for
from flask_login import login_required, current_user, logout_user
from app import db

delete_bp = Blueprint("delete_bp", __name__)

@delete_bp.route("/delete_account", methods=["POST"])
@login_required
def delete_account():
    user = current_user

    # Mark as deleted so chats show "deleted user"
    user.is_deleted = True
    user.f_name = "deleted"
    user.l_name = "user"

    db.session.commit()

    # Now remove the user from the database
    db.session.delete(user)
    db.session.commit()

    logout_user()

    return redirect(url_for("auth.register"))

