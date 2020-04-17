from habr_microblog import app
import cherrypy


cherrypy.tree.graft(app, '/blog/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 5000,
                        'engine.autoreload.on': False,
                        })
cherrypy.engine.start()
# app.run()
