def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_create_job(client):
    response = client.post("/jobs/", json={
        "company": "Google", "role": "Data Engineer",
        "location": "Remote", "status": "applied"
    })
    assert response.status_code == 201
    assert response.json()["company"] == "Google"
    assert response.json()["id"] is not None

def test_get_jobs_empty(client):
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert response.json() == []

def test_get_job_not_found(client):
    response = client.get("/jobs/999")
    assert response.status_code == 404

def test_update_job_status(client):
    create = client.post("/jobs/", json={"company": "Amazon", "role": "SDE"})
    job_id = create.json()["id"]
    response = client.patch(f"/jobs/{job_id}", json={"status": "interview"})
    assert response.status_code == 200
    assert response.json()["status"] == "interview"

def test_delete_job(client):
    create = client.post("/jobs/", json={"company": "Apple", "role": "DE"})
    job_id = create.json()["id"]
    client.delete(f"/jobs/{job_id}")
    assert client.get(f"/jobs/{job_id}").status_code == 404

def test_filter_by_status(client):
    client.post("/jobs/", json={"company": "Netflix", "role": "DE", "status": "applied"})
    client.post("/jobs/", json={"company": "Uber", "role": "MLE", "status": "interview"})
    response = client.get("/jobs/?status=interview")
    assert len(response.json()) == 1
    assert response.json()[0]["company"] == "Uber"

def test_create_job_empty_company_fails(client):
    response = client.post("/jobs/", json={"company": "  ", "role": "DE"})
    assert response.status_code == 422