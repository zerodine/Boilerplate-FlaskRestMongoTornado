from flaskboilerplate import app

# the toolbar is only enabled in debug mode:
app.debug = True
# toolbar = DebugToolbarExtension(coreApp)

app.run(debug=True)