from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ContactForm, SkillForm, CertificationForm, MilestoneForm
from .models import ContactMessage, Skill, Certification, Milestone


def home(request):
    return render(request, 'core/home.html')


def about(request):
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    milestones = Milestone.objects.all()                                                       

    return render(request, 'core/about.html', {
        'skills': skills,
        'certifications': certifications,
        'milestones': milestones
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=contact.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

            send_mail(
                subject="Thanks for contacting me",
                message="I received your message and will reply soon.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
            )

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})



@staff_member_required
def manage_messages(request):
    messages = ContactMessage.objects.all().order_by('-id')
    return render(request, 'core/manage_messages.html', {'messages': messages})


@staff_member_required
def delete_message(request, pk):
    message = get_object_or_404(ContactMessage, pk=pk)

    if request.method == 'POST':
        message.delete()
        return redirect('manage_messages')

    return render(request, 'core/delete_message.html', {'message': message})




@staff_member_required
def manage_skills(request):
    skills = Skill.objects.all()
    return render(request, 'core/manage_skills.html', {'skills': skills})


@staff_member_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_skills')
    else:
        form = SkillForm()

    return render(request, 'core/add_skill.html', {'form': form})


@staff_member_required
def edit_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('manage_skills')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'core/edit_skill.html', {'form': form})


@staff_member_required
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('manage_skills')

    return render(request, 'core/delete_skill.html', {'skill': skill})




@staff_member_required
def manage_certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'core/manage_certifications.html', {
        'certifications': certifications
    })


@staff_member_required
def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_certifications')
    else:
        form = CertificationForm()

    return render(request, 'core/add_certification.html', {'form': form})


@staff_member_required
def edit_certification(request, pk):
    cert = get_object_or_404(Certification, pk=pk)

    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=cert)
        if form.is_valid():
            form.save()
            return redirect('manage_certifications')
    else:
        form = CertificationForm(instance=cert)

    return render(request, 'core/edit_certification.html', {'form': form})


@staff_member_required
def delete_certification(request, pk):
    cert = get_object_or_404(Certification, pk=pk)

    if request.method == 'POST':
        cert.delete()
        return redirect('manage_certifications')

    return render(request, 'core/delete_certification.html', {'cert': cert})

@staff_member_required
def add_milestone(request):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_milestones')
    else:
        form = MilestoneForm()
    return render(request, 'core/add_milestone.html', {'form': form})


@staff_member_required
def manage_milestones(request):
    milestones = Milestone.objects.all()
    return render(request, 'core/manage_milestones.html', {'milestones': milestones})


@staff_member_required
def edit_milestone(request, pk):
    milestone = Milestone.objects.get(pk=pk)
    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('manage_milestones')
    else:
        form = MilestoneForm(instance=milestone)
    return render(request, 'core/edit_milestone.html', {'form': form})


@staff_member_required
def delete_milestone(request, pk):
    milestone = Milestone.objects.get(pk=pk)
    if request.method == 'POST':
        milestone.delete()
        return redirect('manage_milestones')
    return render(request, 'core/delete_milestone.html', {'milestone': milestone})