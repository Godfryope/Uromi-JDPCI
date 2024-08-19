from django.views.generic import TemplateView
from .models import Event, Message, Subscription, Testimonial
from .forms import MessageForm, SubscriptionForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'Events/index.html'  # The template that includes Event, Message Us, Subscribe sections, and Testimonials

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['form'] = MessageForm()
        context['subscription_form'] = SubscriptionForm()
        context['testimonials'] = Testimonial.objects.all()  # Add testimonials to the context
        return context

    def post(self, request, *args, **kwargs):
        # Check which form is submitted
        form_type = request.POST.get('form_type')

        # Handling the "Message Us" form submission
        if form_type == 'message_form':
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                return self.get(request, *args, **kwargs)  # Refresh the page with form data cleared
            else:
                context = self.get_context_data()
                context['form'] = form
                context['subscription_form'] = SubscriptionForm()
                context['testimonials'] = Testimonial.objects.all()  # Include testimonials in the context
                return self.render_to_response(context)
        
        # Handling the "Subscribe" form submission
        elif form_type == 'subscription_form':
            subscription_form = SubscriptionForm(request.POST)
            if subscription_form.is_valid():
                subscription_form.save()
                return self.get(request, *args, **kwargs)  # Refresh the page with form data cleared
            else:
                context = self.get_context_data()
                context['form'] = MessageForm()
                context['subscription_form'] = subscription_form
                context['testimonials'] = Testimonial.objects.all()  # Include testimonials in the context
                return self.render_to_response(context)
        
        # Fallback for invalid form submission
        context = self.get_context_data()
        return self.render_to_response(context)
