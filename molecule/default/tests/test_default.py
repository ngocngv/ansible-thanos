import os
import pytest
import testinfra.utils.ansible_runner

# uses https://testinfra.readthedocs.io/en/latest/modules.html#modules

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
    ('/etc/systemd/system/thanos-query.service', ['thanos query', 'THANOS_QUERY_CLUSTER_HTTP'])
    ('/etc/systemd/system/thanos-sidecar.service', ['thanos sidecar', 'THANOS_SIDECAR_CLUSTER_HTTP'])
    ('/etc/systemd/system/thanos-store.service', ['thanos store', 'THANOS_STORE_CLUSTER_HTTP'])
    ('/etc/systemd/system/thanos-compactor.service', ['thanos compact', 'THANOS_COMPACTOR_HTTP'])
])
def test_config_file_exists(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('svc', [
    'thanos-query',
    'thanos-sidecar',
    'thanos-store',
    'thanos-compactor'
])
def test_service_enabled(host, svc):
    service = host.service(svc)
    assert service.is_enabled
