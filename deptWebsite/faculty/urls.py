from django.urls import path

from .views import (
    edit_basic,
    faculty_detail,
    faculty_page,
    show_affiliation,
    show_award,
    show_book_publications,
    show_conf_publications,
    show_events,
    show_journal_publications,
    show_patent,
    show_pgd,
    show_phd,
    show_projects,
    show_responsibility,
)

urlpatterns = [
    path("", faculty_page, name="faculty_page"),
    path("profile/<int:id>", faculty_detail, name="profile"),
    path("profile/edit/basic/<int:id>", edit_basic, name="profile"),
    path(
        "profile/show/journal-publications/<int:person_id>",
        show_journal_publications,
        name="journal",
    ),
    path(
        "profile/show/conf-publications/<int:person_id>",
        show_conf_publications,
        name="conf",
    ),
    path(
        "profile/show/book-publications/<int:person_id>",
        show_book_publications,
        name="book",
    ),
    path(
        "profile/show/projects/<int:person_id>",
        show_projects,
        name="projects",
    ),
    path(
        "profile/show/events/<int:person_id>",
        show_events,
        name="events",
    ),
    path(
        "profile/show/affiliation/<int:person_id>",
        show_affiliation,
        name="affiliation",
    ),
    path(
        "profile/show/phd/<int:person_id>",
        show_phd,
        name="phd",
    ),
    path(
        "profile/show/pgd/<int:person_id>",
        show_pgd,
        name="pgd",
    ),
    path(
        "profile/show/patent/<int:person_id>",
        show_patent,
        name="patent",
    ),
    path(
        "profile/show/responsibility/<int:person_id>",
        show_responsibility,
        name="responsibility",
    ),
    path(
        "profile/show/awards/<int:person_id>",
        show_award,
        name="award",
    ),
]
