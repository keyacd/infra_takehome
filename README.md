## Takehome

### Installation
You will need [Docker](https://docs.docker.com/engine/install/), as well as a kubernetes cluster (see below.)
Once the prerequisites are set up, use the command `helm install birds helm/birds` to install.
To run just the python portions of the application, install python3, then `pip install requirements.txt`.

### Testing
The bash script `helm_test.sh` will un- then re-install birds, and then run all of its tests.
The templates for these tests can be found in `helm/birds/templates/tests/`.
#### test-connection
This test verifies if the service can connect. Expected result: **success**
#### test-nonstate
This test verifies if the service fails when fed the non-state abbreviation 'pp'. Expected result: **failure**
#### test-pennsylvania
This test verifies if the service returns successfully when fed the state value 'pa'. Expected result: **success**

### This Project Has Got Problems

There are a number of issues with this project.  The goal is to identify and fix as many of the problems as you can and get it to deploy to kubernetes successfully.  If you don't feel like fixing a particular problem, just write down what you would have done so we can discuss it together.

If you don't have a kubernetes cluster handy, you can deploy one locally with [kind](https://kind.sigs.k8s.io/).

Please don't take this as a reflection of the work we do here.  We promise it's not this bad. The goal here is to have you show us that you can debug stuff you didn't write and get it working when needed.

If you have worked or are working on something else that you're more interested in or proud of, and that you can share, feel free to send that back instead of completing this project.
