from django.urls import path

from .views import (
    add_profile_link,
    add_research_info,
    edit_affiliation,
    edit_award,
    edit_basic,
    edit_book_pub,
    edit_conf_pub,
    edit_event,
    edit_journal_pub,
    edit_patent,
    edit_pgd,
    edit_phd,
    edit_profile_links,
    edit_project,
    edit_research_info,
    edit_responsibility,
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
    GeneratePdf
)

urlpatterns = [
    path("", faculty_page, name="faculty_page"),
    path("profile/<int:id>", faculty_detail, name="profile"),
    path("profile/edit/basic/<int:id>", edit_basic, name="edit_profile"),
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
    path("profile/edit/journal_publication/<int:id>", edit_journal_pub, name="Journal"),
    path(
        "profile/edit/conference_publication/<int:id>", edit_conf_pub, name="Conference"
    ),
    path("profile/edit/book_publication/<int:id>", edit_book_pub, name="Book"),
    path("profile/edit/project/<int:id>", edit_project, name="Project"),
    path("profile/edit/event/<int:id>", edit_event, name="Events"),
    path("profile/edit/affiliation/<int:id>", edit_affiliation, name="Affiliation"),
    path("profile/edit/phd_guided/<int:id>", edit_phd, name="PHD Scholars Guided"),
    path("profile/edit/pgd_guided/<int:id>", edit_pgd, name="PGD Guided"),
    path("profile/edit/patent/<int:id>", edit_patent, name="Patent"),
    path("profile/edit/profile_links/<int:id>", edit_profile_links, name="links"),
    path(
        "profile/edit/research_info/<int:id>",
        edit_research_info,
        name="edit_research_info",
    ),
    path(
        "profile/edit/responsibility/<int:id>",
        edit_responsibility,
        name="Responsibility",
    ),
    path("profile/edit/award/<int:id>", edit_award, name="Awards"),
    path("profile/add/profile_link", add_profile_link, name="add_profile_link"),
    path("profile/add/research_info", add_research_info, name="add_research_profile"),
    path('profile/<int:id>/pdf/', GeneratePdf.as_view(),name="pdf"), 

]
