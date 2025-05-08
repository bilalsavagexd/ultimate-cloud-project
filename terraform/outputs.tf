<<<<<<< HEAD
output "vpc_id" {
  value = aws_vpc.main.id
}

output "service_public_ip" {
  value = aws_ecs_service.flask_app.network_configuration[0].assign_public_ip
}
=======
output "vpc_id" {
  value = aws_vpc.main.id
}

output "service_public_ip" {
  value = aws_ecs_service.flask_app.network_configuration[0].assign_public_ip
}
>>>>>>> adddd9c236f0de6cd5aa034f8a9a1d43aed864fb
