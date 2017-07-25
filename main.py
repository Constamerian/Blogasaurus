#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2

Homepage = """
<html>
  <head>
    <link rel="stylesheet" href ="/resources/Jasmine.css">
    <title>All About Jasmine</title>
  </head>
  <body>
    <center>
    <h1>Learn about Me!</h1>
    </center>
    <h2>About me</h2>
      <p>Hello! My name is Jasmine and I'm from Brooklyn, New York. I'm 18 years old
         and I'm a Chinese-American girl.
    <h2>Some things I like:</h2>
      <center>
        <div>
      <a href ="https://www.youtube.com/watch?v=cwqtK2wSjpY">
      <img src ="/resources/music.jpg" id="music"/></a>
      <a href ="/resources/JasminesPhotos.html">
      <img src ="/resources/photography.jpeg" id="photography"/></a>
      <a href ="http://www.xn--h1ame.xn--80adxhks/upload/iblock/40e/40eb848c29ba03e204de822262f1c6a3.jpg">
      <img src ="/resources/food.jpg" id="food"/></a>
        </div>
    </center>
    <h2>Fun facts about me:</h2>
      <ul>
        <li>I will be attending Stony Brook University this fall</li>
        <li>I love cats (yay cats!)</li>
        <li>I love gaming and I tend to stay up late doing so :]</li>
      </ul>
    <center>
      <img src ="/resources/SBU.jpg" id="SBU"/>
      <img src ="/resources/kitten.gif" id="kitten"/>
      <img src ="/resources/gaming.gif" id="gaming"/>
    </center>
    <h2>Some of my favorite shows to watch:</h2>
    <center>
      <div id="shows">
      <a href ="https://www.youtube.com/watch?v=q1pcpgREQ5c">
      <img src ="/resources/greys.jpg" id="greys"/></a>
      <a href ="https://www.youtube.com/watch?v=C2SlnhppBLA">
      <img src ="/resources/ncisla.jpg" id="ncisla"/></a>
      <a href ="https://www.youtube.com/watch?v=ul8gZIGZbdc">
      <img src ="/resources/csimiami.jpg" id="csimiami"/></a>
      <a href ="https://www.youtube.com/watch?v=prE0lIZOqbk">
      <img src ="/resources/scandal.jpg" id="scandal"/></a>
    </div>
    </center>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="/resources/Jasmine.js"></script>
  </body>
</html>

"""

PhotoPage = """
<html>
  <head>
    <link rel="stylesheet" href ="JasminesPhotos.css">
  </head>
  <body>
    <div id ="background"></div>
    <img src= "star.gif" id="star"/>
    <center>
    <h1>Photos I have taken!</h1>
    <img src = "bridge.jpeg" id="bridge"/>
    <img src = "centralpark.jpg" id="park"/>
    <img src = "lotus.jpg" id="lotus"/>
  </center><br>
  <center>
    <img src = "parking.jpg" id="parking"/>
    <img src = "trainstation.jpg" id="station"/>
    <img src = "picture.jpeg" id="pic"/>
  </center>
  </body>
</html>

"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(Homepage)

class PhotoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(PhotoPage)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/photos', PhotoHandler)

], debug=True)
