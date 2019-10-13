from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def analysis(request):
    if 'login' in request.session:
        c = {}
        c.update(csrf(request))
        return render_to_response('analysis.html', c)
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def index(request):
    if 'login' in request.session:
        c = {}
        c.update(csrf(request))
        return render_to_response('index.html', c)
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def generic(request):
    if 'login' in request.session:
        c = {}
        c.update(csrf(request))
        return render_to_response('generic.html', c)
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def elements(request):
    if 'login' in request.session:
        c = {}
        c.update(csrf(request))
        return render_to_response('elements.html', c)
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def tweetdata(request):
    if 'login' in request.session:
        from tweepy import API
        from tweepy import Cursor
        from tweepy.streaming import StreamListener
        from tweepy import OAuthHandler
        from tweepy import Stream
        import io
        import json
        import time
        import datetime

        ACCESS_TOKEN = ""
        ACCESS_TOKEN_SECRET = ""
        CONSUMER_KEY = ""
        CONSUMER_SECRET = ""

        class TwitterClient():
            def __init__(self, twitter_user,fetched_tweets_filename):
                self.auth = TwitterAuthenticator().authenticate_twitter_app()
                self.twitter_client = API(self.auth,wait_on_rate_limit=True)
                self.twitter_user = twitter_user
                self.fetched_tweets_filename = fetched_tweets_filename

            def get_user_timeline_tweets(self,query,num_tweets):
                with io.open(fetched_tweets_filename, "w", encoding="utf-8") as tf:
                    tf.write('[')
                oldest=''
                c=0
                for tweet in Cursor(self.twitter_client.search,q=query).items(200):
                    c+=1
                    t=tweet._json
                    with io.open(fetched_tweets_filename, "a", encoding="utf-8") as tf:
                        json.dump(t,tf)
                        if c<num_tweets:
                            tf.write(',')
                    if c%200==0:
                        oldest=tweet.id-1
                    print(c)
                    if c==num_tweets:
                        with io.open(fetched_tweets_filename, "a", encoding="utf-8") as tf:
                            tf.write(']')
                        return True
                while(1):
                    for tweet in Cursor(self.twitter_client.search,q=query,max_id=oldest).items(200):
                        c+=1
                        t=tweet._json
                        with io.open(fetched_tweets_filename, "a", encoding="utf-8") as tf:
                            json.dump(t,tf)
                            if c<num_tweets:
                                tf.write(',')
                        if c%200==0:
                            oldest=tweet.id-1
                        print(c)
                        if c==num_tweets:
                            with io.open(fetched_tweets_filename, "a", encoding="utf-8") as tf:
                                tf.write(']')
                            return True
                return True


        class TwitterAuthenticator():
            def authenticate_twitter_app(self):
                auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
                return auth
        
        
        if __name__ == '__main__':
            hashtaglist=request.POST.get('hashtaglist', '')
            num_tweets=int(request.POST.get('num_tweets', ''))
            num_days=int(request.POST.get('num_days', ''))
            date=datetime.today() - timedelta(days=num_days)
            fetched_tweets_filename=str(hashtaglist)+'.json'
            twitter_client = TwitterClient(fetched_tweets_filename)
            twitter_client.get_user_timeline_tweets(hashtaglist,num_tweets)
            return HttpResponseRedirect('/analysis/analysis')
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def analysis(request):
    if 'login' in request.session:
        print()
    else:
        c = {}
        c.update(csrf(request))
        return HttpResponseRedirect('/login/')
