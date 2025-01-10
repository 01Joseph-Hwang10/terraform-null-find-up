
variable "targets" {
  description = "File or directory or list of them to search for"
}

variable "cwd" {
  type     = string
  nullable = true
  default  = null
}
