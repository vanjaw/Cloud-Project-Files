# API file to launch for a cowsay similar interaction in regards to
# getting the twitter pronoun data

from flask import Flask, jsonify
import workerApp
import subprocess
import sys
import os

app = Flask(__name__)

old_num_workers = 0

def initiate_workers(num_meshes):
    num_workers = num_meshes % 5
	worker_command = 'openstack stack update $STACK_NAME -t ../openstack/ssc-test-stack.template --parameter "API_UNAME=$OS_USERNAME;API_PWD=$OS_PASSWORD;node_count="' + num_workers + "\""
	os.system(worker_command)

	old_num_workers = num_workers

	return (True)

@app.route('/', methods=['POST', 'GET'])
def initial():
    error = None
    if request.method == 'POST':
        if initiate_workers(request.form['meshes']):
        	print('Workers initiated')
        else:
            error = 'Invalid mesh input'
    
    # The code below is to handle workers
    # 
    # for workers:
    # 	data_index = workerApp.analyze_meshes()
	#
	# ready=data_index.ready()
	# while (ready_last_index==False):
	# 	ready=data_index.ready()
	#	if (ready):
	#		ready=data_next_index.ready()
	# 
 	# tempData=Alldata.get(timeout=1)
	# return(tempData)
    
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    
    return render_template('init.html', error=error)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)