"""Offline adaptation boundaries, not provider or hardware benchmarks."""
from pathlib import Path
from unittest.mock import patch
import pytest

def test_separate_home(monkeypatch,tmp_path):
    from nanobot.config.home import get_home_path,set_home_path
    set_home_path(None)
    monkeypatch.setattr(Path,'home',lambda:tmp_path)
    assert get_home_path()==tmp_path/'.vyana'

def test_launcher_uses_inherited_runtime():
    from vyana.cli import main
    with patch('nanobot.cli.entry.main') as upstream:
        main()
        upstream.assert_called_once_with()

def test_upstream_installation_disabled():
    from nanobot.update import update_installation
    with pytest.raises(RuntimeError,match='Vyana automatic updates are disabled'):
        update_installation()

def test_upstream_staging_disabled():
    from nanobot.update_service import UpdateJobService
    with pytest.raises(RuntimeError,match='Vyana automatic update'):
        UpdateJobService().prepare('untrusted-plan')

@pytest.mark.asyncio
async def test_upstream_execution_disabled():
    from nanobot.update_service import UpdateJobService
    with pytest.raises(RuntimeError,match='Vyana automatic update'):
        await UpdateJobService().execute('untrusted-plan')
