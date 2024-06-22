step1: create a python flask project
step2: Containerizing the Basic Python Application by creating a Dockerfile in the project directory
step3: Build the Docker image, run the following Docker command:
        docker build -t raahulsharma96/flask-hello-world:latest .
step4: Initiating a Docker Container using command :
        docker run -p 5000:5000 raahulsharma96/flask-hello-world:latest

step5: Pushing the Docker Image to Docker Hub
        docker login
        docker push raahulsharma96/flask-hello-world:latest
step6: Launching the Minikube Kubernetes Cluster
        minikube config set driver docker
        minikube start
        kubectl version
step7: Creating the deployment.yaml  file for the Kubernetes Deployment
step8: Creating the service.yaml file for the Kubernetes Service
step9: To create this Kubernetes Deployment, execute this subsequent kubectl command:
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
step10: Getting Information about the Kubernetes Deployment and Service
        kubectl get deployment
        kubectl get service
        minikube service list
        minikube service my-flask-service

