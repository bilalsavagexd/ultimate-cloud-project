output "vpc_id" {
  value = aws_vpc.main.id
}
output "load_balancer_dns" {
  value = aws_lb.app_lb.dns_name
}
