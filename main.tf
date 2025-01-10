
data "external" "find_up" {
  program = [
    "python3",
    "${path.module}/scripts/find_up.py"
  ]

  query = {
    "targets" = join(",", var.targets)
    "cwd"     = var.cwd
  }
}

