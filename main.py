import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "North London Boxing Training"
        subtitle = "Boxing and Fitness training"
        description = "From cardio training to advance fitness courses, Jake Foley offers expert boxing training that has the power to transform his clients."
        keywords = "north london boxing training,strength training sessions,personal trainer,cardio training, advance fitness courses, jake foley,expert boxing training"
        banner = "<picture><img src=\"/images/other/jake.png\" width=\"960\" height=\"378\" alt=\"North London Boxing Training\" /></picture>"
        # banner="<div id=\"video\"><video autoplay=\"autoplay\" poster=\"/images/other/jake.png\" loop><source src=\"/videos/jake.ogv\" type=\"video/ogg\"><source src=\"/videos/jake.webm\" type=\"video/webm\"><source src=\"/videos/jake.mp4\" type=\"video/mp4\"></video></div>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("index.html")
        self.response.write(template.render(template_vars))

class StoryHandler(webapp2.RequestHandler):
    def get(self):
        title = "About Us"
        subtitle = "Discover your inner strength and learn how to box"
        description = "Jake Foley is the head personal trainer for North London Boxing Training."
        keywords = "london,north london,cardio,boxing,personal trainer,fitness,jake foley,north london boxing training"
        banner = "<picture><source srcset=\"/images/banner/banner.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner.jpg\" width=\"960\" height=\"378\" alt=\"North London Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("about.html")
        self.response.write(template.render(template_vars))

class WhatsInvolvedHandler(webapp2.RequestHandler):
    def get(self):
        title = "Training"
        subtitle = "Professional Boxing training to achieve your goals"
        description = "From strength training to footwork drills and pad work, we offer professional training that will help you achieve your goals."
        keywords = "london,north london,professional boxing training,cardio,boxing,personal trainer,fitness,footwork drills,bag work,pad work,core training,cardio training,strength training"
        banner = "<picture><source srcset=\"/images/banner/banner_2.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_2.jpg\" width=\"960\" height=\"378\" alt=\"North London Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("whats-involved.html")
        self.response.write(template.render(template_vars))

class GetInTouchHandler(webapp2.RequestHandler):
    def get(self):
        title = "Get in touch"
        subtitle = "Discover the boxer within, and get in touch today."
        description = "Unleash the boxer within by hiring Jake Foley to be your personal trainer."
        keywords = "jake foley,boxer,personal trainer,london,north london,cardio,boxing,fitness"
        banner = "<picture><source srcset=\"/images/banner/banner_3.svg\" type=\"image/svg+xml\"><img src=\"/images/banner/banner_3.jpg\" width=\"960\" height=\"378\" alt=\"North London Boxing Training\" /></picture>"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"banner": banner}
        template = JINJA_ENVIRONMENT.get_template("get-in-touch.html")
        self.response.write(template.render(template_vars))

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        title = "Basics"
        subtitle = "Boxing Basics"
        description = "Boxing is a sport that requires intense workout without having to tear your muscles and joints."
        keywords = "jake foley,boxing,sport,workout,muscles,joints"
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords}
        template = JINJA_ENVIRONMENT.get_template("blog.html")
        self.response.write(template.render(template_vars))

class ArticlesHandler(webapp2.RequestHandler):
    def get(self):
        title = "Boxing Tips For Beginners"
        subtitle = "It all starts in the mirror"
        description = "The best beginner boxing tip one can give is to first improve their whole body strenghts"
        keywords = "boxing tip,beginner boxing,heavy bag,boxing training,jab,muscles,workouts"
        path = self.request.path
        template_vars = {"title":title,"subtitle":subtitle,"description":description,"keywords": keywords,"path":path}
        template = JINJA_ENVIRONMENT.get_template("articles.html")
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about.html', StoryHandler),
    ('/whats-involved.html', WhatsInvolvedHandler),
    ('/get-in-touch.html', GetInTouchHandler),
    ('/blog.html', BlogHandler),
    ('/.*', ArticlesHandler),
], debug=True)
