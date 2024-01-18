# config/deploy/local.rb
server ENV['SERVER_IP'], user: 'ubuntu', roles: %w{app}

set :deploy_to, '/home/ubuntu/challenge/fastapi-vizz-challenge'

set :ssh_options, {
  keys: [ENV['SERVER_KEY_FILE']],
  forward_agent: false,
  auth_methods: %w(publickey)
}


after 'deploy:starting', 'exporter:deploy'
after 'exporter:deploy', 'importer:deploy'
after 'importer:deploy', 'deploy:restart_services'


