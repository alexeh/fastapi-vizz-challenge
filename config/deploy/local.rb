# config/deploy/local.rb
server ENV['SERVER_IP'], user: 'ubuntu', roles: %w{app}

set :deploy_to, ENV['DEPLOYMENT_PATH']

set :ssh_options, {
  keys: [ENV['SERVER_KEY_FILE']],
  forward_agent: false,
  auth_methods: %w(publickey)
}


after 'deploy:starting', 'exporter:deploy'
after 'exporter:deploy', 'importer:deploy'
after 'importer:deploy', 'deploy:restart_services'
# after 'deploy:restart_services', 'deploy:health_exporter'
# after 'deploy:health_exporter', 'deploy:health_importer'


