from fastapi.testclient import TestClient
import pytest

from exporter.db.database import get_mongo_client
from exporter.main import asgi_app

client = TestClient(asgi_app)


@pytest.fixture(scope="session", autouse=True)
def handle_db():
    mongo_client = get_mongo_client()
    mongo_client.insert_many(get_mock_data())

    yield

    mongo_client.delete_many({})


def test_get_emissions():
    response = client.get("/emissions")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_emissions_country_filter():
    print('NO PINTA NADA O QUE')
    response = client.get("/emissions?country=USA")
    assert response.status_code == 200
    results = response.json()
    for item in results:
        assert item["country"] == "USA"


def test_get_emissions_sector_filter():
    response = client.get("/emissions?sector=Energy")
    assert response.status_code == 200
    results = response.json()
    for item in results:
        assert item["sector"] == "Energy"


def test_get_emissions_year_filter():
    response = client.get("/emissions?year=2000")
    assert response.status_code == 200
    results = response.json()
    for item in results:
        assert any(value["year"] == 2000 for value in item["valuesPerYear"])


def test_get_emissions_value_filter():
    response = client.get("/emissions?value=12.34")
    assert response.status_code == 200
    results = response.json()
    for item in results:
        assert any(value["value"] == 12.34 for value in item["valuesPerYear"])


def test_get_emissions_pagination():
    response = client.get("/emissions?skip=0&limit=1")
    assert response.status_code == 200
    results = response.json()
    assert len(results) == 1


def test_get_emissions_sorting():
    response = client.get("/emissions?sort_by=country&sort_order=desc")
    assert response.status_code == 200
    results = response.json()
    if len(results) > 1:
        assert results[0]["country"] >= results[1]["country"]


def get_mock_data():
    return [
        {
            "country": "ABW",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 0.0419
                },
                {
                    "year": 1851,
                    "value": 0.0441
                },
                {
                    "year": 1852,
                    "value": 0.0465
                },
                {
                    "year": 1853,
                    "value": 0.049
                },
                {
                    "year": 1854,
                    "value": 0.0517
                },
                {
                    "year": 1855,
                    "value": 0.0545
                },
                {
                    "year": 1856,
                    "value": 0.0575
                },
                {
                    "year": 1857,
                    "value": 0.0606
                },
                {
                    "year": 1858,
                    "value": 0.0638
                },
                {
                    "year": 1859,
                    "value": 0.0671
                },
                {
                    "year": 1860,
                    "value": 0.0706
                },
                {
                    "year": 1861,
                    "value": 0.0741
                },
                {
                    "year": 1862,
                    "value": 0.0778
                },
                {
                    "year": 1863,
                    "value": 0.0817
                },
                {
                    "year": 1864,
                    "value": 0.0858
                },
                {
                    "year": 1865,
                    "value": 0.09
                },
                {
                    "year": 1866,
                    "value": 0.0945
                },
                {
                    "year": 1867,
                    "value": 0.0991
                },
                {
                    "year": 1868,
                    "value": 0.104
                },
                {
                    "year": 1869,
                    "value": 0.109
                },
                {
                    "year": 1870,
                    "value": 0.114
                },
                {
                    "year": 1871,
                    "value": 0.12
                },
                {
                    "year": 1872,
                    "value": 0.126
                },
                {
                    "year": 1873,
                    "value": 0.132
                },
                {
                    "year": 1874,
                    "value": 0.139
                },
                {
                    "year": 1875,
                    "value": 0.145
                },
                {
                    "year": 1876,
                    "value": 0.153
                },
                {
                    "year": 1877,
                    "value": 0.16
                },
                {
                    "year": 1878,
                    "value": 0.167
                },
                {
                    "year": 1879,
                    "value": 0.175
                },
                {
                    "year": 1880,
                    "value": 0.183
                },
                {
                    "year": 1881,
                    "value": 0.191
                },
                {
                    "year": 1882,
                    "value": 0.199
                },
                {
                    "year": 1883,
                    "value": 0.208
                },
                {
                    "year": 1884,
                    "value": 0.216
                },
                {
                    "year": 1885,
                    "value": 0.226
                },
                {
                    "year": 1886,
                    "value": 0.235
                },
                {
                    "year": 1887,
                    "value": 0.245
                },
                {
                    "year": 1888,
                    "value": 0.255
                },
                {
                    "year": 1889,
                    "value": 0.265
                },
                {
                    "year": 1890,
                    "value": 0.297
                },
                {
                    "year": 1891,
                    "value": 0.308
                },
                {
                    "year": 1892,
                    "value": 0.321
                },
                {
                    "year": 1893,
                    "value": 0.335
                },
                {
                    "year": 1894,
                    "value": 0.351
                },
                {
                    "year": 1895,
                    "value": 0.367
                },
                {
                    "year": 1896,
                    "value": 0.385
                },
                {
                    "year": 1897,
                    "value": 0.403
                },
                {
                    "year": 1898,
                    "value": 0.422
                },
                {
                    "year": 1899,
                    "value": 0.442
                },
                {
                    "year": 1900,
                    "value": 0.463
                },
                {
                    "year": 1901,
                    "value": 0.485
                },
                {
                    "year": 1902,
                    "value": 0.51
                },
                {
                    "year": 1903,
                    "value": 0.537
                },
                {
                    "year": 1904,
                    "value": 0.565
                },
                {
                    "year": 1905,
                    "value": 0.595
                },
                {
                    "year": 1906,
                    "value": 0.625
                },
                {
                    "year": 1907,
                    "value": 0.655
                },
                {
                    "year": 1908,
                    "value": 0.686
                },
                {
                    "year": 1909,
                    "value": 0.715
                },
                {
                    "year": 1910,
                    "value": 0.744
                },
                {
                    "year": 1911,
                    "value": 0.771
                },
                {
                    "year": 1912,
                    "value": 0.798
                },
                {
                    "year": 1913,
                    "value": 0.824
                },
                {
                    "year": 1914,
                    "value": 0.85
                },
                {
                    "year": 1915,
                    "value": 0.876
                },
                {
                    "year": 1916,
                    "value": 0.903
                },
                {
                    "year": 1917,
                    "value": 0.93
                },
                {
                    "year": 1918,
                    "value": 0.958
                },
                {
                    "year": 1919,
                    "value": 0.987
                },
                {
                    "year": 1920,
                    "value": 1.02
                },
                {
                    "year": 1921,
                    "value": 1.05
                },
                {
                    "year": 1922,
                    "value": 1.08
                },
                {
                    "year": 1923,
                    "value": 1.12
                },
                {
                    "year": 1924,
                    "value": 1.15
                },
                {
                    "year": 1925,
                    "value": 1.42
                },
                {
                    "year": 1926,
                    "value": 1.83
                },
                {
                    "year": 1927,
                    "value": 1.8
                },
                {
                    "year": 1928,
                    "value": 4.72
                },
                {
                    "year": 1929,
                    "value": 5.92
                },
                {
                    "year": 1930,
                    "value": 7.25
                },
                {
                    "year": 1931,
                    "value": 6.17
                },
                {
                    "year": 1932,
                    "value": 5.99
                },
                {
                    "year": 1933,
                    "value": 6.39
                },
                {
                    "year": 1934,
                    "value": 7.12
                },
                {
                    "year": 1935,
                    "value": 8.22
                },
                {
                    "year": 1936,
                    "value": 8.78
                },
                {
                    "year": 1937,
                    "value": 10.6
                },
                {
                    "year": 1938,
                    "value": 11.4
                },
                {
                    "year": 1939,
                    "value": 10.7
                },
                {
                    "year": 1940,
                    "value": 8.87
                },
                {
                    "year": 1941,
                    "value": 11.0
                },
                {
                    "year": 1942,
                    "value": 6.39
                },
                {
                    "year": 1943,
                    "value": 10.3
                },
                {
                    "year": 1944,
                    "value": 12.9
                },
                {
                    "year": 1945,
                    "value": 15.0
                },
                {
                    "year": 1946,
                    "value": 16.5
                },
                {
                    "year": 1947,
                    "value": 18.2
                },
                {
                    "year": 1948,
                    "value": 18.5
                },
                {
                    "year": 1949,
                    "value": 9.85
                },
                {
                    "year": 1950,
                    "value": 1.2
                },
                {
                    "year": 1951,
                    "value": 1.89
                },
                {
                    "year": 1952,
                    "value": 1.09
                },
                {
                    "year": 1953,
                    "value": 1.26
                },
                {
                    "year": 1954,
                    "value": 2.56
                },
                {
                    "year": 1955,
                    "value": 2.11
                },
                {
                    "year": 1956,
                    "value": 2.74
                },
                {
                    "year": 1957,
                    "value": 1.87
                },
                {
                    "year": 1958,
                    "value": 1.64
                },
                {
                    "year": 1959,
                    "value": 2.11
                },
                {
                    "year": 1960,
                    "value": 1.81
                },
                {
                    "year": 1961,
                    "value": 1.89
                },
                {
                    "year": 1962,
                    "value": 2.08
                },
                {
                    "year": 1963,
                    "value": 1.99
                },
                {
                    "year": 1964,
                    "value": 1.93
                },
                {
                    "year": 1965,
                    "value": 1.73
                },
                {
                    "year": 1966,
                    "value": 1.62
                },
                {
                    "year": 1967,
                    "value": 2.0
                },
                {
                    "year": 1968,
                    "value": 1.86
                },
                {
                    "year": 1969,
                    "value": 2.43
                },
                {
                    "year": 1970,
                    "value": 2.71
                },
                {
                    "year": 1971,
                    "value": 2.36
                },
                {
                    "year": 1972,
                    "value": 2.29
                },
                {
                    "year": 1973,
                    "value": 2.54
                },
                {
                    "year": 1974,
                    "value": 2.3
                },
                {
                    "year": 1975,
                    "value": 1.68
                },
                {
                    "year": 1976,
                    "value": 3.55
                },
                {
                    "year": 1977,
                    "value": 1.87
                },
                {
                    "year": 1978,
                    "value": 1.59
                },
                {
                    "year": 1979,
                    "value": 1.67
                },
                {
                    "year": 1980,
                    "value": 1.72
                },
                {
                    "year": 1981,
                    "value": 1.64
                },
                {
                    "year": 1982,
                    "value": 1.83
                },
                {
                    "year": 1983,
                    "value": 0.957
                },
                {
                    "year": 1984,
                    "value": 2.34
                },
                {
                    "year": 1985,
                    "value": 2.73
                },
                {
                    "year": 1986,
                    "value": 0.214
                },
                {
                    "year": 1987,
                    "value": 0.481
                },
                {
                    "year": 1988,
                    "value": 0.646
                },
                {
                    "year": 1989,
                    "value": 0.683
                },
                {
                    "year": 1990,
                    "value": 1.77
                },
                {
                    "year": 1991,
                    "value": 1.81
                },
                {
                    "year": 1992,
                    "value": 1.6
                },
                {
                    "year": 1993,
                    "value": 1.64
                },
                {
                    "year": 1994,
                    "value": 1.64
                },
                {
                    "year": 1995,
                    "value": 1.65
                },
                {
                    "year": 1996,
                    "value": 1.66
                },
                {
                    "year": 1997,
                    "value": 1.7
                },
                {
                    "year": 1998,
                    "value": 1.76
                },
                {
                    "year": 1999,
                    "value": 1.8
                },
                {
                    "year": 2000,
                    "value": 2.37
                },
                {
                    "year": 2001,
                    "value": 2.41
                },
                {
                    "year": 2002,
                    "value": 2.42
                },
                {
                    "year": 2003,
                    "value": 2.47
                },
                {
                    "year": 2004,
                    "value": 2.47
                },
                {
                    "year": 2005,
                    "value": 2.55
                },
                {
                    "year": 2006,
                    "value": 2.55
                },
                {
                    "year": 2007,
                    "value": 2.65
                },
                {
                    "year": 2008,
                    "value": 2.57
                },
                {
                    "year": 2009,
                    "value": 2.58
                },
                {
                    "year": 2010,
                    "value": 2.52
                },
                {
                    "year": 2011,
                    "value": 2.5
                },
                {
                    "year": 2012,
                    "value": 1.36
                },
                {
                    "year": 2013,
                    "value": 0.935
                },
                {
                    "year": 2014,
                    "value": 1.07
                }
            ]
        },
        {
            "country": "AFG",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 0.0803
                },
                {
                    "year": 1851,
                    "value": 0.0803
                },
                {
                    "year": 1852,
                    "value": 0.0803
                },
                {
                    "year": 1853,
                    "value": 0.0803
                },
                {
                    "year": 1854,
                    "value": 0.0804
                },
                {
                    "year": 1855,
                    "value": 0.0804
                },
                {
                    "year": 1856,
                    "value": 0.0804
                },
                {
                    "year": 1857,
                    "value": 0.0804
                },
                {
                    "year": 1858,
                    "value": 0.0804
                },
                {
                    "year": 1859,
                    "value": 0.0804
                },
                {
                    "year": 1860,
                    "value": 0.0805
                },
                {
                    "year": 1861,
                    "value": 0.175
                },
                {
                    "year": 1862,
                    "value": 0.193
                },
                {
                    "year": 1863,
                    "value": 0.21
                },
                {
                    "year": 1864,
                    "value": 0.218
                },
                {
                    "year": 1865,
                    "value": 0.225
                },
                {
                    "year": 1866,
                    "value": 0.232
                },
                {
                    "year": 1867,
                    "value": 0.238
                },
                {
                    "year": 1868,
                    "value": 0.243
                },
                {
                    "year": 1869,
                    "value": 0.249
                },
                {
                    "year": 1870,
                    "value": 0.254
                },
                {
                    "year": 1871,
                    "value": 0.259
                },
                {
                    "year": 1872,
                    "value": 0.263
                },
                {
                    "year": 1873,
                    "value": 0.267
                },
                {
                    "year": 1874,
                    "value": 0.272
                },
                {
                    "year": 1875,
                    "value": 0.276
                },
                {
                    "year": 1876,
                    "value": 0.279
                },
                {
                    "year": 1877,
                    "value": 0.282
                },
                {
                    "year": 1878,
                    "value": 0.285
                },
                {
                    "year": 1879,
                    "value": 0.288
                },
                {
                    "year": 1880,
                    "value": 0.29
                },
                {
                    "year": 1881,
                    "value": 0.293
                },
                {
                    "year": 1882,
                    "value": 0.296
                },
                {
                    "year": 1883,
                    "value": 0.298
                },
                {
                    "year": 1884,
                    "value": 0.301
                },
                {
                    "year": 1885,
                    "value": 0.304
                },
                {
                    "year": 1886,
                    "value": 0.306
                },
                {
                    "year": 1887,
                    "value": 0.309
                },
                {
                    "year": 1888,
                    "value": 0.311
                },
                {
                    "year": 1889,
                    "value": 0.314
                },
                {
                    "year": 1890,
                    "value": 0.316
                },
                {
                    "year": 1891,
                    "value": 0.319
                },
                {
                    "year": 1892,
                    "value": 0.321
                },
                {
                    "year": 1893,
                    "value": 0.323
                },
                {
                    "year": 1894,
                    "value": 0.326
                },
                {
                    "year": 1895,
                    "value": 0.328
                },
                {
                    "year": 1896,
                    "value": 0.33
                },
                {
                    "year": 1897,
                    "value": 0.332
                },
                {
                    "year": 1898,
                    "value": 0.334
                },
                {
                    "year": 1899,
                    "value": 0.337
                },
                {
                    "year": 1900,
                    "value": 0.339
                },
                {
                    "year": 1901,
                    "value": 0.386
                },
                {
                    "year": 1902,
                    "value": 0.396
                },
                {
                    "year": 1903,
                    "value": 0.405
                },
                {
                    "year": 1904,
                    "value": 0.41
                },
                {
                    "year": 1905,
                    "value": 0.414
                },
                {
                    "year": 1906,
                    "value": 0.418
                },
                {
                    "year": 1907,
                    "value": 0.421
                },
                {
                    "year": 1908,
                    "value": 0.424
                },
                {
                    "year": 1909,
                    "value": 0.427
                },
                {
                    "year": 1910,
                    "value": 0.43
                },
                {
                    "year": 1911,
                    "value": 0.433
                },
                {
                    "year": 1912,
                    "value": 0.435
                },
                {
                    "year": 1913,
                    "value": 0.437
                },
                {
                    "year": 1914,
                    "value": 0.439
                },
                {
                    "year": 1915,
                    "value": 0.441
                },
                {
                    "year": 1916,
                    "value": 0.442
                },
                {
                    "year": 1917,
                    "value": 0.443
                },
                {
                    "year": 1918,
                    "value": 0.444
                },
                {
                    "year": 1919,
                    "value": 0.445
                },
                {
                    "year": 1920,
                    "value": 0.445
                },
                {
                    "year": 1921,
                    "value": 0.445
                },
                {
                    "year": 1922,
                    "value": 0.446
                },
                {
                    "year": 1923,
                    "value": 0.446
                },
                {
                    "year": 1924,
                    "value": 0.446
                },
                {
                    "year": 1925,
                    "value": 0.446
                },
                {
                    "year": 1926,
                    "value": 0.609
                },
                {
                    "year": 1927,
                    "value": 0.645
                },
                {
                    "year": 1928,
                    "value": 0.678
                },
                {
                    "year": 1929,
                    "value": 0.686
                },
                {
                    "year": 1930,
                    "value": 0.693
                },
                {
                    "year": 1931,
                    "value": 0.705
                },
                {
                    "year": 1932,
                    "value": 0.716
                },
                {
                    "year": 1933,
                    "value": 0.728
                },
                {
                    "year": 1934,
                    "value": 0.739
                },
                {
                    "year": 1935,
                    "value": 0.749
                },
                {
                    "year": 1936,
                    "value": 0.76
                },
                {
                    "year": 1937,
                    "value": 0.769
                },
                {
                    "year": 1938,
                    "value": 0.779
                },
                {
                    "year": 1939,
                    "value": 0.788
                },
                {
                    "year": 1940,
                    "value": 0.796
                },
                {
                    "year": 1941,
                    "value": 0.804
                },
                {
                    "year": 1942,
                    "value": 0.811
                },
                {
                    "year": 1943,
                    "value": 0.818
                },
                {
                    "year": 1944,
                    "value": 0.824
                },
                {
                    "year": 1945,
                    "value": 0.83
                },
                {
                    "year": 1946,
                    "value": 0.836
                },
                {
                    "year": 1947,
                    "value": 0.842
                },
                {
                    "year": 1948,
                    "value": 0.849
                },
                {
                    "year": 1949,
                    "value": 0.842
                },
                {
                    "year": 1950,
                    "value": 0.923
                },
                {
                    "year": 1951,
                    "value": 0.763
                },
                {
                    "year": 1952,
                    "value": 0.736
                },
                {
                    "year": 1953,
                    "value": 0.712
                },
                {
                    "year": 1954,
                    "value": 0.681
                },
                {
                    "year": 1955,
                    "value": 0.688
                },
                {
                    "year": 1956,
                    "value": 0.71
                },
                {
                    "year": 1957,
                    "value": 0.816
                },
                {
                    "year": 1958,
                    "value": 0.846
                },
                {
                    "year": 1959,
                    "value": 0.896
                },
                {
                    "year": 1960,
                    "value": 0.924
                },
                {
                    "year": 1961,
                    "value": 0.994
                },
                {
                    "year": 1962,
                    "value": 1.2
                },
                {
                    "year": 1963,
                    "value": 1.21
                },
                {
                    "year": 1964,
                    "value": 1.34
                },
                {
                    "year": 1965,
                    "value": 1.51
                },
                {
                    "year": 1966,
                    "value": 1.63
                },
                {
                    "year": 1967,
                    "value": 1.84
                },
                {
                    "year": 1968,
                    "value": 1.8
                },
                {
                    "year": 1969,
                    "value": 1.5
                },
                {
                    "year": 1970,
                    "value": 2.22
                },
                {
                    "year": 1971,
                    "value": 2.45
                },
                {
                    "year": 1972,
                    "value": 2.1
                },
                {
                    "year": 1973,
                    "value": 2.2
                },
                {
                    "year": 1974,
                    "value": 2.49
                },
                {
                    "year": 1975,
                    "value": 2.71
                },
                {
                    "year": 1976,
                    "value": 2.6
                },
                {
                    "year": 1977,
                    "value": 2.99
                },
                {
                    "year": 1978,
                    "value": 2.74
                },
                {
                    "year": 1979,
                    "value": 2.81
                },
                {
                    "year": 1980,
                    "value": 2.34
                },
                {
                    "year": 1981,
                    "value": 2.47
                },
                {
                    "year": 1982,
                    "value": 2.59
                },
                {
                    "year": 1983,
                    "value": 3.0
                },
                {
                    "year": 1984,
                    "value": 3.36
                },
                {
                    "year": 1985,
                    "value": 4.07
                },
                {
                    "year": 1986,
                    "value": 3.7
                },
                {
                    "year": 1987,
                    "value": 3.7
                },
                {
                    "year": 1988,
                    "value": 3.45
                },
                {
                    "year": 1989,
                    "value": 3.37
                },
                {
                    "year": 1990,
                    "value": 3.21
                },
                {
                    "year": 1991,
                    "value": 2.97
                },
                {
                    "year": 1992,
                    "value": 1.93
                },
                {
                    "year": 1993,
                    "value": 1.87
                },
                {
                    "year": 1994,
                    "value": 1.77
                },
                {
                    "year": 1995,
                    "value": 1.73
                },
                {
                    "year": 1996,
                    "value": 1.67
                },
                {
                    "year": 1997,
                    "value": 1.58
                },
                {
                    "year": 1998,
                    "value": 1.53
                },
                {
                    "year": 1999,
                    "value": 1.31
                },
                {
                    "year": 2000,
                    "value": 1.3
                },
                {
                    "year": 2001,
                    "value": 1.17
                },
                {
                    "year": 2002,
                    "value": 1.41
                },
                {
                    "year": 2003,
                    "value": 1.56
                },
                {
                    "year": 2004,
                    "value": 1.49
                },
                {
                    "year": 2005,
                    "value": 1.88
                },
                {
                    "year": 2006,
                    "value": 2.2
                },
                {
                    "year": 2007,
                    "value": 2.82
                },
                {
                    "year": 2008,
                    "value": 4.77
                },
                {
                    "year": 2009,
                    "value": 7.34
                },
                {
                    "year": 2010,
                    "value": 9.03
                },
                {
                    "year": 2011,
                    "value": 12.8
                },
                {
                    "year": 2012,
                    "value": 21.0
                },
                {
                    "year": 2013,
                    "value": 21.9
                },
                {
                    "year": 2014,
                    "value": 25.0
                }
            ]
        },
        {
            "country": "AGO",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": -0.611
                },
                {
                    "year": 1851,
                    "value": -0.484
                },
                {
                    "year": 1852,
                    "value": -0.42
                },
                {
                    "year": 1853,
                    "value": -0.447
                },
                {
                    "year": 1854,
                    "value": -0.41
                },
                {
                    "year": 1855,
                    "value": -0.495
                },
                {
                    "year": 1856,
                    "value": -0.476
                },
                {
                    "year": 1857,
                    "value": -0.494
                },
                {
                    "year": 1858,
                    "value": -0.633
                },
                {
                    "year": 1859,
                    "value": -0.755
                },
                {
                    "year": 1860,
                    "value": -0.878
                },
                {
                    "year": 1861,
                    "value": -1.0
                },
                {
                    "year": 1862,
                    "value": -0.937
                },
                {
                    "year": 1863,
                    "value": -0.788
                },
                {
                    "year": 1864,
                    "value": -0.554
                },
                {
                    "year": 1865,
                    "value": -0.232
                },
                {
                    "year": 1866,
                    "value": -0.114
                },
                {
                    "year": 1867,
                    "value": 0.0038
                },
                {
                    "year": 1868,
                    "value": 0.0194
                },
                {
                    "year": 1869,
                    "value": -0.0968
                },
                {
                    "year": 1870,
                    "value": -0.213
                },
                {
                    "year": 1871,
                    "value": -0.327
                },
                {
                    "year": 1872,
                    "value": -0.441
                },
                {
                    "year": 1873,
                    "value": -0.312
                },
                {
                    "year": 1874,
                    "value": -0.106
                },
                {
                    "year": 1875,
                    "value": -0.0031
                },
                {
                    "year": 1876,
                    "value": 0.1
                },
                {
                    "year": 1877,
                    "value": 0.118
                },
                {
                    "year": 1878,
                    "value": 0.136
                },
                {
                    "year": 1879,
                    "value": 0.153
                },
                {
                    "year": 1880,
                    "value": 0.0495
                },
                {
                    "year": 1881,
                    "value": -0.044
                },
                {
                    "year": 1882,
                    "value": -0.137
                },
                {
                    "year": 1883,
                    "value": -0.244
                },
                {
                    "year": 1884,
                    "value": -0.107
                },
                {
                    "year": 1885,
                    "value": 0.0294
                },
                {
                    "year": 1886,
                    "value": 0.166
                },
                {
                    "year": 1887,
                    "value": 0.208
                },
                {
                    "year": 1888,
                    "value": 0.13
                },
                {
                    "year": 1889,
                    "value": 0.0276
                },
                {
                    "year": 1890,
                    "value": 0.0465
                },
                {
                    "year": 1891,
                    "value": -0.0935
                },
                {
                    "year": 1892,
                    "value": -0.234
                },
                {
                    "year": 1893,
                    "value": -0.457
                },
                {
                    "year": 1894,
                    "value": -0.643
                },
                {
                    "year": 1895,
                    "value": -0.551
                },
                {
                    "year": 1896,
                    "value": -0.563
                },
                {
                    "year": 1897,
                    "value": -0.388
                },
                {
                    "year": 1898,
                    "value": -0.212
                },
                {
                    "year": 1899,
                    "value": -0.163
                },
                {
                    "year": 1900,
                    "value": -0.228
                },
                {
                    "year": 1901,
                    "value": -0.296
                },
                {
                    "year": 1902,
                    "value": 0.00252
                },
                {
                    "year": 1903,
                    "value": 0.689
                },
                {
                    "year": 1904,
                    "value": 1.61
                },
                {
                    "year": 1905,
                    "value": 2.81
                },
                {
                    "year": 1906,
                    "value": 4.26
                },
                {
                    "year": 1907,
                    "value": 5.77
                },
                {
                    "year": 1908,
                    "value": 7.28
                },
                {
                    "year": 1909,
                    "value": 8.72
                },
                {
                    "year": 1910,
                    "value": 10.0
                },
                {
                    "year": 1911,
                    "value": 11.3
                },
                {
                    "year": 1912,
                    "value": 12.7
                },
                {
                    "year": 1913,
                    "value": 13.9
                },
                {
                    "year": 1914,
                    "value": 15.1
                },
                {
                    "year": 1915,
                    "value": 16.3
                },
                {
                    "year": 1916,
                    "value": 17.5
                },
                {
                    "year": 1917,
                    "value": 19.0
                },
                {
                    "year": 1918,
                    "value": 20.2
                },
                {
                    "year": 1919,
                    "value": 21.5
                },
                {
                    "year": 1920,
                    "value": 22.8
                },
                {
                    "year": 1921,
                    "value": 23.9
                },
                {
                    "year": 1922,
                    "value": 24.9
                },
                {
                    "year": 1923,
                    "value": 25.9
                },
                {
                    "year": 1924,
                    "value": 26.7
                },
                {
                    "year": 1925,
                    "value": 27.5
                },
                {
                    "year": 1926,
                    "value": 28.3
                },
                {
                    "year": 1927,
                    "value": 29.0
                },
                {
                    "year": 1928,
                    "value": 30.0
                },
                {
                    "year": 1929,
                    "value": 30.9
                },
                {
                    "year": 1930,
                    "value": 31.8
                },
                {
                    "year": 1931,
                    "value": 32.8
                },
                {
                    "year": 1932,
                    "value": 33.7
                },
                {
                    "year": 1933,
                    "value": 34.8
                },
                {
                    "year": 1934,
                    "value": 35.8
                },
                {
                    "year": 1935,
                    "value": 37.4
                },
                {
                    "year": 1936,
                    "value": 38.3
                },
                {
                    "year": 1937,
                    "value": 39.4
                },
                {
                    "year": 1938,
                    "value": 40.5
                },
                {
                    "year": 1939,
                    "value": 41.7
                },
                {
                    "year": 1940,
                    "value": 43.0
                },
                {
                    "year": 1941,
                    "value": 44.0
                },
                {
                    "year": 1942,
                    "value": 45.3
                },
                {
                    "year": 1943,
                    "value": 46.5
                },
                {
                    "year": 1944,
                    "value": 47.8
                },
                {
                    "year": 1945,
                    "value": 49.1
                },
                {
                    "year": 1946,
                    "value": 50.5
                },
                {
                    "year": 1947,
                    "value": 51.8
                },
                {
                    "year": 1948,
                    "value": 53.9
                },
                {
                    "year": 1949,
                    "value": 56.0
                },
                {
                    "year": 1950,
                    "value": 58.3
                },
                {
                    "year": 1951,
                    "value": 60.7
                },
                {
                    "year": 1952,
                    "value": 58.9
                },
                {
                    "year": 1953,
                    "value": 60.5
                },
                {
                    "year": 1954,
                    "value": 62.2
                },
                {
                    "year": 1955,
                    "value": 64.2
                },
                {
                    "year": 1956,
                    "value": 66.1
                },
                {
                    "year": 1957,
                    "value": 68.0
                },
                {
                    "year": 1958,
                    "value": 69.6
                },
                {
                    "year": 1959,
                    "value": 71.2
                },
                {
                    "year": 1960,
                    "value": 72.7
                },
                {
                    "year": 1961,
                    "value": 73.8
                },
                {
                    "year": 1962,
                    "value": 75.0
                },
                {
                    "year": 1963,
                    "value": 77.9
                },
                {
                    "year": 1964,
                    "value": 79.0
                },
                {
                    "year": 1965,
                    "value": 80.5
                },
                {
                    "year": 1966,
                    "value": 80.3
                },
                {
                    "year": 1967,
                    "value": 80.3
                },
                {
                    "year": 1968,
                    "value": 78.7
                },
                {
                    "year": 1969,
                    "value": 83.8
                },
                {
                    "year": 1970,
                    "value": 80.9
                },
                {
                    "year": 1971,
                    "value": 82.5
                },
                {
                    "year": 1972,
                    "value": 85.7
                },
                {
                    "year": 1973,
                    "value": 88.2
                },
                {
                    "year": 1974,
                    "value": 90.3
                },
                {
                    "year": 1975,
                    "value": 84.3
                },
                {
                    "year": 1976,
                    "value": 91.2
                },
                {
                    "year": 1977,
                    "value": 82.2
                },
                {
                    "year": 1978,
                    "value": 87.8
                },
                {
                    "year": 1979,
                    "value": 88.6
                },
                {
                    "year": 1980,
                    "value": 85.3
                },
                {
                    "year": 1981,
                    "value": 97.4
                },
                {
                    "year": 1982,
                    "value": 105.0
                },
                {
                    "year": 1983,
                    "value": 113.0
                },
                {
                    "year": 1984,
                    "value": 119.0
                },
                {
                    "year": 1985,
                    "value": 114.0
                },
                {
                    "year": 1986,
                    "value": 112.0
                },
                {
                    "year": 1987,
                    "value": 113.0
                },
                {
                    "year": 1988,
                    "value": 117.0
                },
                {
                    "year": 1989,
                    "value": 114.0
                },
                {
                    "year": 1990,
                    "value": 116.0
                },
                {
                    "year": 1991,
                    "value": 113.0
                },
                {
                    "year": 1992,
                    "value": 124.0
                },
                {
                    "year": 1993,
                    "value": 130.0
                },
                {
                    "year": 1994,
                    "value": 138.0
                },
                {
                    "year": 1995,
                    "value": 156.0
                },
                {
                    "year": 1996,
                    "value": 155.0
                },
                {
                    "year": 1997,
                    "value": 144.0
                },
                {
                    "year": 1998,
                    "value": 156.0
                },
                {
                    "year": 1999,
                    "value": 155.0
                },
                {
                    "year": 2000,
                    "value": 154.0
                },
                {
                    "year": 2001,
                    "value": 154.0
                },
                {
                    "year": 2002,
                    "value": 155.0
                },
                {
                    "year": 2003,
                    "value": 134.0
                },
                {
                    "year": 2004,
                    "value": 144.0
                },
                {
                    "year": 2005,
                    "value": 151.0
                },
                {
                    "year": 2006,
                    "value": 97.5
                },
                {
                    "year": 2007,
                    "value": 117.0
                },
                {
                    "year": 2008,
                    "value": 103.0
                },
                {
                    "year": 2009,
                    "value": 106.0
                },
                {
                    "year": 2010,
                    "value": 110.0
                },
                {
                    "year": 2011,
                    "value": 132.0
                },
                {
                    "year": 2012,
                    "value": 112.0
                },
                {
                    "year": 2013,
                    "value": 122.0
                },
                {
                    "year": 2014,
                    "value": 112.0
                }
            ]
        },
        {
            "country": "AIA",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 0.000164
                },
                {
                    "year": 1851,
                    "value": 0.000173
                },
                {
                    "year": 1852,
                    "value": 0.000182
                },
                {
                    "year": 1853,
                    "value": 0.000192
                },
                {
                    "year": 1854,
                    "value": 0.000203
                },
                {
                    "year": 1855,
                    "value": 0.000214
                },
                {
                    "year": 1856,
                    "value": 0.000225
                },
                {
                    "year": 1857,
                    "value": 0.000238
                },
                {
                    "year": 1858,
                    "value": 0.00025
                },
                {
                    "year": 1859,
                    "value": 0.000263
                },
                {
                    "year": 1860,
                    "value": 0.000277
                },
                {
                    "year": 1861,
                    "value": 0.000291
                },
                {
                    "year": 1862,
                    "value": 0.000305
                },
                {
                    "year": 1863,
                    "value": 0.00032
                },
                {
                    "year": 1864,
                    "value": 0.000336
                },
                {
                    "year": 1865,
                    "value": 0.000353
                },
                {
                    "year": 1866,
                    "value": 0.00037
                },
                {
                    "year": 1867,
                    "value": 0.000389
                },
                {
                    "year": 1868,
                    "value": 0.000408
                },
                {
                    "year": 1869,
                    "value": 0.000427
                },
                {
                    "year": 1870,
                    "value": 0.000448
                },
                {
                    "year": 1871,
                    "value": 0.00047
                },
                {
                    "year": 1872,
                    "value": 0.000493
                },
                {
                    "year": 1873,
                    "value": 0.000517
                },
                {
                    "year": 1874,
                    "value": 0.000543
                },
                {
                    "year": 1875,
                    "value": 0.00057
                },
                {
                    "year": 1876,
                    "value": 0.000598
                },
                {
                    "year": 1877,
                    "value": 0.000627
                },
                {
                    "year": 1878,
                    "value": 0.000656
                },
                {
                    "year": 1879,
                    "value": 0.000687
                },
                {
                    "year": 1880,
                    "value": 0.000717
                },
                {
                    "year": 1881,
                    "value": 0.000749
                },
                {
                    "year": 1882,
                    "value": 0.000781
                },
                {
                    "year": 1883,
                    "value": 0.000814
                },
                {
                    "year": 1884,
                    "value": 0.000849
                },
                {
                    "year": 1885,
                    "value": 0.000884
                },
                {
                    "year": 1886,
                    "value": 0.000921
                },
                {
                    "year": 1887,
                    "value": 0.000959
                },
                {
                    "year": 1888,
                    "value": 0.000998
                },
                {
                    "year": 1889,
                    "value": 0.00104
                },
                {
                    "year": 1890,
                    "value": 0.00108
                },
                {
                    "year": 1891,
                    "value": 0.00113
                },
                {
                    "year": 1892,
                    "value": 0.00117
                },
                {
                    "year": 1893,
                    "value": 0.00122
                },
                {
                    "year": 1894,
                    "value": 0.00127
                },
                {
                    "year": 1895,
                    "value": 0.00132
                },
                {
                    "year": 1896,
                    "value": 0.00138
                },
                {
                    "year": 1897,
                    "value": 0.00144
                },
                {
                    "year": 1898,
                    "value": 0.0015
                },
                {
                    "year": 1899,
                    "value": 0.00156
                },
                {
                    "year": 1900,
                    "value": 0.00162
                },
                {
                    "year": 1901,
                    "value": 0.0017
                },
                {
                    "year": 1902,
                    "value": 0.00178
                },
                {
                    "year": 1903,
                    "value": 0.00188
                },
                {
                    "year": 1904,
                    "value": 0.00198
                },
                {
                    "year": 1905,
                    "value": 0.00208
                },
                {
                    "year": 1906,
                    "value": 0.00218
                },
                {
                    "year": 1907,
                    "value": 0.00227
                },
                {
                    "year": 1908,
                    "value": 0.00236
                },
                {
                    "year": 1909,
                    "value": 0.00243
                },
                {
                    "year": 1910,
                    "value": 0.00249
                },
                {
                    "year": 1911,
                    "value": 0.00254
                },
                {
                    "year": 1912,
                    "value": 0.00258
                },
                {
                    "year": 1913,
                    "value": 0.00261
                },
                {
                    "year": 1914,
                    "value": 0.00265
                },
                {
                    "year": 1915,
                    "value": 0.00268
                },
                {
                    "year": 1916,
                    "value": 0.00271
                },
                {
                    "year": 1917,
                    "value": 0.00274
                },
                {
                    "year": 1918,
                    "value": 0.00277
                },
                {
                    "year": 1919,
                    "value": 0.0028
                },
                {
                    "year": 1920,
                    "value": 0.00283
                },
                {
                    "year": 1921,
                    "value": 0.00287
                },
                {
                    "year": 1922,
                    "value": 0.0029
                },
                {
                    "year": 1923,
                    "value": 0.00293
                },
                {
                    "year": 1924,
                    "value": 0.00297
                },
                {
                    "year": 1925,
                    "value": 0.003
                },
                {
                    "year": 1926,
                    "value": 0.00303
                },
                {
                    "year": 1927,
                    "value": 0.00307
                },
                {
                    "year": 1928,
                    "value": 0.00311
                },
                {
                    "year": 1929,
                    "value": 0.00315
                },
                {
                    "year": 1930,
                    "value": 0.0032
                },
                {
                    "year": 1931,
                    "value": 0.00325
                },
                {
                    "year": 1932,
                    "value": 0.00331
                },
                {
                    "year": 1933,
                    "value": 0.00338
                },
                {
                    "year": 1934,
                    "value": 0.00345
                },
                {
                    "year": 1935,
                    "value": 0.00353
                },
                {
                    "year": 1936,
                    "value": 0.00361
                },
                {
                    "year": 1937,
                    "value": 0.00369
                },
                {
                    "year": 1938,
                    "value": 0.00378
                },
                {
                    "year": 1939,
                    "value": 0.00386
                },
                {
                    "year": 1940,
                    "value": 0.00395
                },
                {
                    "year": 1941,
                    "value": 0.00403
                },
                {
                    "year": 1942,
                    "value": 0.00412
                },
                {
                    "year": 1943,
                    "value": 0.0042
                },
                {
                    "year": 1944,
                    "value": 0.00428
                },
                {
                    "year": 1945,
                    "value": 0.00437
                },
                {
                    "year": 1946,
                    "value": 0.00447
                },
                {
                    "year": 1947,
                    "value": 0.00457
                },
                {
                    "year": 1948,
                    "value": 0.00469
                },
                {
                    "year": 1949,
                    "value": 0.00481
                },
                {
                    "year": 1950,
                    "value": 0.00496
                },
                {
                    "year": 1951,
                    "value": 0.00512
                },
                {
                    "year": 1952,
                    "value": 0.00533
                },
                {
                    "year": 1953,
                    "value": 0.00557
                },
                {
                    "year": 1954,
                    "value": 0.00584
                },
                {
                    "year": 1955,
                    "value": 0.00614
                },
                {
                    "year": 1956,
                    "value": 0.00646
                },
                {
                    "year": 1957,
                    "value": 0.00679
                },
                {
                    "year": 1958,
                    "value": 0.00713
                },
                {
                    "year": 1959,
                    "value": 0.00748
                },
                {
                    "year": 1960,
                    "value": 0.00783
                },
                {
                    "year": 1961,
                    "value": 0.00821
                },
                {
                    "year": 1962,
                    "value": 0.00863
                },
                {
                    "year": 1963,
                    "value": 0.00908
                },
                {
                    "year": 1964,
                    "value": 0.00955
                },
                {
                    "year": 1965,
                    "value": 0.0113
                },
                {
                    "year": 1966,
                    "value": 0.012
                },
                {
                    "year": 1967,
                    "value": 0.0122
                },
                {
                    "year": 1968,
                    "value": 0.013
                },
                {
                    "year": 1969,
                    "value": 0.0135
                },
                {
                    "year": 1970,
                    "value": 0.0144
                },
                {
                    "year": 1971,
                    "value": 0.0188
                },
                {
                    "year": 1972,
                    "value": 0.02
                },
                {
                    "year": 1973,
                    "value": 0.0209
                },
                {
                    "year": 1974,
                    "value": 0.0227
                },
                {
                    "year": 1975,
                    "value": 0.0215
                },
                {
                    "year": 1976,
                    "value": 0.021
                },
                {
                    "year": 1977,
                    "value": 0.0231
                },
                {
                    "year": 1978,
                    "value": 0.0253
                },
                {
                    "year": 1979,
                    "value": 0.0276
                },
                {
                    "year": 1980,
                    "value": 0.0305
                },
                {
                    "year": 1981,
                    "value": 0.032
                },
                {
                    "year": 1982,
                    "value": 0.0296
                },
                {
                    "year": 1983,
                    "value": 0.0317
                },
                {
                    "year": 1984,
                    "value": 0.0299
                },
                {
                    "year": 1985,
                    "value": 0.0278
                },
                {
                    "year": 1986,
                    "value": 0.0334
                },
                {
                    "year": 1987,
                    "value": 0.0345
                },
                {
                    "year": 1988,
                    "value": 0.0338
                },
                {
                    "year": 1989,
                    "value": 0.034
                },
                {
                    "year": 1990,
                    "value": 0.035
                },
                {
                    "year": 1991,
                    "value": 0.0353
                },
                {
                    "year": 1992,
                    "value": 0.0343
                },
                {
                    "year": 1993,
                    "value": 0.0361
                },
                {
                    "year": 1994,
                    "value": 0.0368
                },
                {
                    "year": 1995,
                    "value": 0.0396
                },
                {
                    "year": 1996,
                    "value": 0.0402
                },
                {
                    "year": 1997,
                    "value": 0.044
                },
                {
                    "year": 1998,
                    "value": 0.0477
                },
                {
                    "year": 1999,
                    "value": 0.0513
                },
                {
                    "year": 2000,
                    "value": 0.0623
                },
                {
                    "year": 2001,
                    "value": 0.0953
                },
                {
                    "year": 2002,
                    "value": 0.0953
                },
                {
                    "year": 2003,
                    "value": 0.103
                },
                {
                    "year": 2004,
                    "value": 0.121
                },
                {
                    "year": 2005,
                    "value": 0.128
                },
                {
                    "year": 2006,
                    "value": 0.195
                },
                {
                    "year": 2007,
                    "value": 0.203
                },
                {
                    "year": 2008,
                    "value": 0.203
                },
                {
                    "year": 2009,
                    "value": 0.199
                },
                {
                    "year": 2010,
                    "value": 0.203
                },
                {
                    "year": 2011,
                    "value": 0.147
                },
                {
                    "year": 2012,
                    "value": 0.147
                },
                {
                    "year": 2013,
                    "value": 0.139
                },
                {
                    "year": 2014,
                    "value": 0.14
                }
            ]
        },
        {
            "country": "ALB",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 2.11
                },
                {
                    "year": 1851,
                    "value": 2.11
                },
                {
                    "year": 1852,
                    "value": 2.1
                },
                {
                    "year": 1853,
                    "value": 2.1
                },
                {
                    "year": 1854,
                    "value": 2.1
                },
                {
                    "year": 1855,
                    "value": 2.1
                },
                {
                    "year": 1856,
                    "value": 2.1
                },
                {
                    "year": 1857,
                    "value": 2.1
                },
                {
                    "year": 1858,
                    "value": 2.1
                },
                {
                    "year": 1859,
                    "value": 2.1
                },
                {
                    "year": 1860,
                    "value": 2.1
                },
                {
                    "year": 1861,
                    "value": 2.1
                },
                {
                    "year": 1862,
                    "value": 2.11
                },
                {
                    "year": 1863,
                    "value": 2.11
                },
                {
                    "year": 1864,
                    "value": 2.11
                },
                {
                    "year": 1865,
                    "value": 2.12
                },
                {
                    "year": 1866,
                    "value": 2.12
                },
                {
                    "year": 1867,
                    "value": 2.13
                },
                {
                    "year": 1868,
                    "value": 2.13
                },
                {
                    "year": 1869,
                    "value": 2.14
                },
                {
                    "year": 1870,
                    "value": 2.14
                },
                {
                    "year": 1871,
                    "value": 1.99
                },
                {
                    "year": 1872,
                    "value": 1.97
                },
                {
                    "year": 1873,
                    "value": 1.94
                },
                {
                    "year": 1874,
                    "value": 1.92
                },
                {
                    "year": 1875,
                    "value": 1.9
                },
                {
                    "year": 1876,
                    "value": 1.88
                },
                {
                    "year": 1877,
                    "value": 1.87
                },
                {
                    "year": 1878,
                    "value": 1.85
                },
                {
                    "year": 1879,
                    "value": 1.84
                },
                {
                    "year": 1880,
                    "value": 1.83
                },
                {
                    "year": 1881,
                    "value": 1.82
                },
                {
                    "year": 1882,
                    "value": 1.81
                },
                {
                    "year": 1883,
                    "value": 1.8
                },
                {
                    "year": 1884,
                    "value": 1.79
                },
                {
                    "year": 1885,
                    "value": 1.78
                },
                {
                    "year": 1886,
                    "value": 1.78
                },
                {
                    "year": 1887,
                    "value": 1.79
                },
                {
                    "year": 1888,
                    "value": 1.8
                },
                {
                    "year": 1889,
                    "value": 1.8
                },
                {
                    "year": 1890,
                    "value": 1.81
                },
                {
                    "year": 1891,
                    "value": 1.82
                },
                {
                    "year": 1892,
                    "value": 1.82
                },
                {
                    "year": 1893,
                    "value": 1.83
                },
                {
                    "year": 1894,
                    "value": 1.84
                },
                {
                    "year": 1895,
                    "value": 1.84
                },
                {
                    "year": 1896,
                    "value": 1.85
                },
                {
                    "year": 1897,
                    "value": 1.85
                },
                {
                    "year": 1898,
                    "value": 1.86
                },
                {
                    "year": 1899,
                    "value": 1.86
                },
                {
                    "year": 1900,
                    "value": 1.87
                },
                {
                    "year": 1901,
                    "value": 1.88
                },
                {
                    "year": 1902,
                    "value": 1.89
                },
                {
                    "year": 1903,
                    "value": 1.89
                },
                {
                    "year": 1904,
                    "value": 1.9
                },
                {
                    "year": 1905,
                    "value": 1.91
                },
                {
                    "year": 1906,
                    "value": 1.92
                },
                {
                    "year": 1907,
                    "value": 1.93
                },
                {
                    "year": 1908,
                    "value": 1.95
                },
                {
                    "year": 1909,
                    "value": 1.96
                },
                {
                    "year": 1910,
                    "value": 1.97
                },
                {
                    "year": 1911,
                    "value": 1.98
                },
                {
                    "year": 1912,
                    "value": 1.99
                },
                {
                    "year": 1913,
                    "value": 2.0
                },
                {
                    "year": 1914,
                    "value": 2.01
                },
                {
                    "year": 1915,
                    "value": 2.02
                },
                {
                    "year": 1916,
                    "value": 2.03
                },
                {
                    "year": 1917,
                    "value": 2.05
                },
                {
                    "year": 1918,
                    "value": 2.06
                },
                {
                    "year": 1919,
                    "value": 2.07
                },
                {
                    "year": 1920,
                    "value": 2.08
                },
                {
                    "year": 1921,
                    "value": 2.1
                },
                {
                    "year": 1922,
                    "value": 2.11
                },
                {
                    "year": 1923,
                    "value": 2.12
                },
                {
                    "year": 1924,
                    "value": 2.14
                },
                {
                    "year": 1925,
                    "value": 2.15
                },
                {
                    "year": 1926,
                    "value": 2.14
                },
                {
                    "year": 1927,
                    "value": 2.13
                },
                {
                    "year": 1928,
                    "value": 2.11
                },
                {
                    "year": 1929,
                    "value": 2.1
                },
                {
                    "year": 1930,
                    "value": 2.08
                },
                {
                    "year": 1931,
                    "value": 2.05
                },
                {
                    "year": 1932,
                    "value": 2.02
                },
                {
                    "year": 1933,
                    "value": 1.96
                },
                {
                    "year": 1934,
                    "value": 1.93
                },
                {
                    "year": 1935,
                    "value": 1.91
                },
                {
                    "year": 1936,
                    "value": 1.98
                },
                {
                    "year": 1937,
                    "value": 2.11
                },
                {
                    "year": 1938,
                    "value": 2.13
                },
                {
                    "year": 1939,
                    "value": 2.18
                },
                {
                    "year": 1940,
                    "value": 2.4
                },
                {
                    "year": 1941,
                    "value": 2.29
                },
                {
                    "year": 1942,
                    "value": 2.37
                },
                {
                    "year": 1943,
                    "value": 2.05
                },
                {
                    "year": 1944,
                    "value": 1.7
                },
                {
                    "year": 1945,
                    "value": 1.62
                },
                {
                    "year": 1946,
                    "value": 1.96
                },
                {
                    "year": 1947,
                    "value": 2.37
                },
                {
                    "year": 1948,
                    "value": 2.11
                },
                {
                    "year": 1949,
                    "value": 2.39
                },
                {
                    "year": 1950,
                    "value": 1.62
                },
                {
                    "year": 1951,
                    "value": 1.7
                },
                {
                    "year": 1952,
                    "value": 1.66
                },
                {
                    "year": 1953,
                    "value": 1.68
                },
                {
                    "year": 1954,
                    "value": 1.76
                },
                {
                    "year": 1955,
                    "value": 1.92
                },
                {
                    "year": 1956,
                    "value": 2.11
                },
                {
                    "year": 1957,
                    "value": 2.79
                },
                {
                    "year": 1958,
                    "value": 2.49
                },
                {
                    "year": 1959,
                    "value": 2.75
                },
                {
                    "year": 1960,
                    "value": 3.35
                },
                {
                    "year": 1961,
                    "value": 3.56
                },
                {
                    "year": 1962,
                    "value": 3.74
                },
                {
                    "year": 1963,
                    "value": 3.36
                },
                {
                    "year": 1964,
                    "value": 3.3
                },
                {
                    "year": 1965,
                    "value": 3.47
                },
                {
                    "year": 1966,
                    "value": 3.86
                },
                {
                    "year": 1967,
                    "value": 4.01
                },
                {
                    "year": 1968,
                    "value": 4.42
                },
                {
                    "year": 1969,
                    "value": 4.62
                },
                {
                    "year": 1970,
                    "value": 5.04
                },
                {
                    "year": 1971,
                    "value": 5.57
                },
                {
                    "year": 1972,
                    "value": 6.81
                },
                {
                    "year": 1973,
                    "value": 6.43
                },
                {
                    "year": 1974,
                    "value": 5.42
                },
                {
                    "year": 1975,
                    "value": 5.48
                },
                {
                    "year": 1976,
                    "value": 5.76
                },
                {
                    "year": 1977,
                    "value": 6.46
                },
                {
                    "year": 1978,
                    "value": 7.19
                },
                {
                    "year": 1979,
                    "value": 8.23
                },
                {
                    "year": 1980,
                    "value": 5.74
                },
                {
                    "year": 1981,
                    "value": 7.89
                },
                {
                    "year": 1982,
                    "value": 7.75
                },
                {
                    "year": 1983,
                    "value": 8.0
                },
                {
                    "year": 1984,
                    "value": 8.23
                },
                {
                    "year": 1985,
                    "value": 8.28
                },
                {
                    "year": 1986,
                    "value": 8.47
                },
                {
                    "year": 1987,
                    "value": 7.85
                },
                {
                    "year": 1988,
                    "value": 7.74
                },
                {
                    "year": 1989,
                    "value": 9.46
                },
                {
                    "year": 1990,
                    "value": 5.78
                },
                {
                    "year": 1991,
                    "value": 4.71
                },
                {
                    "year": 1992,
                    "value": 2.74
                },
                {
                    "year": 1993,
                    "value": 2.58
                },
                {
                    "year": 1994,
                    "value": 2.24
                },
                {
                    "year": 1995,
                    "value": 2.34
                },
                {
                    "year": 1996,
                    "value": 2.25
                },
                {
                    "year": 1997,
                    "value": 1.76
                },
                {
                    "year": 1998,
                    "value": 1.99
                },
                {
                    "year": 1999,
                    "value": 3.22
                },
                {
                    "year": 2000,
                    "value": 3.24
                },
                {
                    "year": 2001,
                    "value": 4.21
                },
                {
                    "year": 2002,
                    "value": 4.77
                },
                {
                    "year": 2003,
                    "value": 5.32
                },
                {
                    "year": 2004,
                    "value": 5.23
                },
                {
                    "year": 2005,
                    "value": 5.31
                },
                {
                    "year": 2006,
                    "value": 3.88
                },
                {
                    "year": 2007,
                    "value": 3.93
                },
                {
                    "year": 2008,
                    "value": 4.37
                },
                {
                    "year": 2009,
                    "value": 4.35
                },
                {
                    "year": 2010,
                    "value": 4.58
                },
                {
                    "year": 2011,
                    "value": 5.1
                },
                {
                    "year": 2012,
                    "value": 4.58
                },
                {
                    "year": 2013,
                    "value": 4.69
                },
                {
                    "year": 2014,
                    "value": 4.95
                }
            ]
        },
        {
            "country": "AND",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 0.00723
                },
                {
                    "year": 1851,
                    "value": 0.0077
                },
                {
                    "year": 1852,
                    "value": 0.00821
                },
                {
                    "year": 1853,
                    "value": 0.00876
                },
                {
                    "year": 1854,
                    "value": 0.00934
                },
                {
                    "year": 1855,
                    "value": 0.00995
                },
                {
                    "year": 1856,
                    "value": 0.0106
                },
                {
                    "year": 1857,
                    "value": 0.0113
                },
                {
                    "year": 1858,
                    "value": 0.0119
                },
                {
                    "year": 1859,
                    "value": 0.0127
                },
                {
                    "year": 1860,
                    "value": 0.0134
                },
                {
                    "year": 1861,
                    "value": 0.0142
                },
                {
                    "year": 1862,
                    "value": 0.015
                },
                {
                    "year": 1863,
                    "value": 0.0158
                },
                {
                    "year": 1864,
                    "value": 0.0167
                },
                {
                    "year": 1865,
                    "value": 0.0176
                },
                {
                    "year": 1866,
                    "value": 0.0186
                },
                {
                    "year": 1867,
                    "value": 0.0196
                },
                {
                    "year": 1868,
                    "value": 0.0207
                },
                {
                    "year": 1869,
                    "value": 0.0218
                },
                {
                    "year": 1870,
                    "value": 0.0229
                },
                {
                    "year": 1871,
                    "value": 0.0237
                },
                {
                    "year": 1872,
                    "value": 0.0249
                },
                {
                    "year": 1873,
                    "value": 0.0262
                },
                {
                    "year": 1874,
                    "value": 0.0275
                },
                {
                    "year": 1875,
                    "value": 0.029
                },
                {
                    "year": 1876,
                    "value": 0.0304
                },
                {
                    "year": 1877,
                    "value": 0.032
                },
                {
                    "year": 1878,
                    "value": 0.0336
                },
                {
                    "year": 1879,
                    "value": 0.0352
                },
                {
                    "year": 1880,
                    "value": 0.0368
                },
                {
                    "year": 1881,
                    "value": 0.0385
                },
                {
                    "year": 1882,
                    "value": 0.0403
                },
                {
                    "year": 1883,
                    "value": 0.0421
                },
                {
                    "year": 1884,
                    "value": 0.0439
                },
                {
                    "year": 1885,
                    "value": 0.0459
                },
                {
                    "year": 1886,
                    "value": 0.0479
                },
                {
                    "year": 1887,
                    "value": 0.05
                },
                {
                    "year": 1888,
                    "value": 0.0522
                },
                {
                    "year": 1889,
                    "value": 0.0545
                },
                {
                    "year": 1890,
                    "value": 0.06
                },
                {
                    "year": 1891,
                    "value": 0.0623
                },
                {
                    "year": 1892,
                    "value": 0.0649
                },
                {
                    "year": 1893,
                    "value": 0.0676
                },
                {
                    "year": 1894,
                    "value": 0.0705
                },
                {
                    "year": 1895,
                    "value": 0.0736
                },
                {
                    "year": 1896,
                    "value": 0.0768
                },
                {
                    "year": 1897,
                    "value": 0.0802
                },
                {
                    "year": 1898,
                    "value": 0.0837
                },
                {
                    "year": 1899,
                    "value": 0.0873
                },
                {
                    "year": 1900,
                    "value": 0.091
                },
                {
                    "year": 1901,
                    "value": 0.0952
                },
                {
                    "year": 1902,
                    "value": 0.0999
                },
                {
                    "year": 1903,
                    "value": 0.105
                },
                {
                    "year": 1904,
                    "value": 0.11
                },
                {
                    "year": 1905,
                    "value": 0.116
                },
                {
                    "year": 1906,
                    "value": 0.122
                },
                {
                    "year": 1907,
                    "value": 0.127
                },
                {
                    "year": 1908,
                    "value": 0.132
                },
                {
                    "year": 1909,
                    "value": 0.136
                },
                {
                    "year": 1910,
                    "value": 0.14
                },
                {
                    "year": 1911,
                    "value": 0.143
                },
                {
                    "year": 1912,
                    "value": 0.146
                },
                {
                    "year": 1913,
                    "value": 0.148
                },
                {
                    "year": 1914,
                    "value": 0.15
                },
                {
                    "year": 1915,
                    "value": 0.153
                },
                {
                    "year": 1916,
                    "value": 0.155
                },
                {
                    "year": 1917,
                    "value": 0.157
                },
                {
                    "year": 1918,
                    "value": 0.159
                },
                {
                    "year": 1919,
                    "value": 0.162
                },
                {
                    "year": 1920,
                    "value": 0.165
                },
                {
                    "year": 1921,
                    "value": 0.168
                },
                {
                    "year": 1922,
                    "value": 0.172
                },
                {
                    "year": 1923,
                    "value": 0.176
                },
                {
                    "year": 1924,
                    "value": 0.181
                },
                {
                    "year": 1925,
                    "value": 0.186
                },
                {
                    "year": 1926,
                    "value": 0.19
                },
                {
                    "year": 1927,
                    "value": 0.194
                },
                {
                    "year": 1928,
                    "value": 0.198
                },
                {
                    "year": 1929,
                    "value": 0.201
                },
                {
                    "year": 1930,
                    "value": 0.203
                },
                {
                    "year": 1931,
                    "value": 0.204
                },
                {
                    "year": 1932,
                    "value": 0.206
                },
                {
                    "year": 1933,
                    "value": 0.207
                },
                {
                    "year": 1934,
                    "value": 0.208
                },
                {
                    "year": 1935,
                    "value": 0.209
                },
                {
                    "year": 1936,
                    "value": 0.21
                },
                {
                    "year": 1937,
                    "value": 0.211
                },
                {
                    "year": 1938,
                    "value": 0.212
                },
                {
                    "year": 1939,
                    "value": 0.212
                },
                {
                    "year": 1940,
                    "value": 0.212
                },
                {
                    "year": 1941,
                    "value": 0.212
                },
                {
                    "year": 1942,
                    "value": 0.21
                },
                {
                    "year": 1943,
                    "value": 0.209
                },
                {
                    "year": 1944,
                    "value": 0.207
                },
                {
                    "year": 1945,
                    "value": 0.205
                },
                {
                    "year": 1946,
                    "value": 0.203
                },
                {
                    "year": 1947,
                    "value": 0.201
                },
                {
                    "year": 1948,
                    "value": 0.199
                },
                {
                    "year": 1949,
                    "value": 0.198
                },
                {
                    "year": 1950,
                    "value": 0.197
                },
                {
                    "year": 1951,
                    "value": 0.198
                },
                {
                    "year": 1952,
                    "value": 0.202
                },
                {
                    "year": 1953,
                    "value": 0.207
                },
                {
                    "year": 1954,
                    "value": 0.214
                },
                {
                    "year": 1955,
                    "value": 0.222
                },
                {
                    "year": 1956,
                    "value": 0.232
                },
                {
                    "year": 1957,
                    "value": 0.242
                },
                {
                    "year": 1958,
                    "value": 0.253
                },
                {
                    "year": 1959,
                    "value": 0.263
                },
                {
                    "year": 1960,
                    "value": 0.274
                },
                {
                    "year": 1961,
                    "value": 0.286
                },
                {
                    "year": 1962,
                    "value": 0.301
                },
                {
                    "year": 1963,
                    "value": 0.319
                },
                {
                    "year": 1964,
                    "value": 0.338
                },
                {
                    "year": 1965,
                    "value": 0.358
                },
                {
                    "year": 1966,
                    "value": 0.377
                },
                {
                    "year": 1967,
                    "value": 0.395
                },
                {
                    "year": 1968,
                    "value": 0.41
                },
                {
                    "year": 1969,
                    "value": 0.422
                },
                {
                    "year": 1970,
                    "value": 0.429
                },
                {
                    "year": 1971,
                    "value": 0.433
                },
                {
                    "year": 1972,
                    "value": 0.445
                },
                {
                    "year": 1973,
                    "value": 0.471
                },
                {
                    "year": 1974,
                    "value": 0.459
                },
                {
                    "year": 1975,
                    "value": 0.437
                },
                {
                    "year": 1976,
                    "value": 0.464
                },
                {
                    "year": 1977,
                    "value": 0.459
                },
                {
                    "year": 1978,
                    "value": 0.47
                },
                {
                    "year": 1979,
                    "value": 0.493
                },
                {
                    "year": 1980,
                    "value": 0.471
                },
                {
                    "year": 1981,
                    "value": 0.45
                },
                {
                    "year": 1982,
                    "value": 0.432
                },
                {
                    "year": 1983,
                    "value": 0.429
                },
                {
                    "year": 1984,
                    "value": 0.43
                },
                {
                    "year": 1985,
                    "value": 0.437
                },
                {
                    "year": 1986,
                    "value": 0.438
                },
                {
                    "year": 1987,
                    "value": 0.441
                },
                {
                    "year": 1988,
                    "value": 0.442
                },
                {
                    "year": 1989,
                    "value": 0.444
                },
                {
                    "year": 1990,
                    "value": 0.444
                },
                {
                    "year": 1991,
                    "value": 0.439
                },
                {
                    "year": 1992,
                    "value": 0.428
                },
                {
                    "year": 1993,
                    "value": 0.42
                },
                {
                    "year": 1994,
                    "value": 0.423
                },
                {
                    "year": 1995,
                    "value": 0.388
                },
                {
                    "year": 1996,
                    "value": 0.406
                },
                {
                    "year": 1997,
                    "value": 0.439
                },
                {
                    "year": 1998,
                    "value": 0.465
                },
                {
                    "year": 1999,
                    "value": 0.494
                },
                {
                    "year": 2000,
                    "value": 0.505
                },
                {
                    "year": 2001,
                    "value": 0.495
                },
                {
                    "year": 2002,
                    "value": 0.503
                },
                {
                    "year": 2003,
                    "value": 0.506
                },
                {
                    "year": 2004,
                    "value": 0.536
                },
                {
                    "year": 2005,
                    "value": 0.547
                },
                {
                    "year": 2006,
                    "value": 0.507
                },
                {
                    "year": 2007,
                    "value": 0.5
                },
                {
                    "year": 2008,
                    "value": 0.5
                },
                {
                    "year": 2009,
                    "value": 0.478
                },
                {
                    "year": 2010,
                    "value": 0.478
                },
                {
                    "year": 2011,
                    "value": 0.47
                },
                {
                    "year": 2012,
                    "value": 0.47
                },
                {
                    "year": 2013,
                    "value": 0.47
                },
                {
                    "year": 2014,
                    "value": 0.484
                }
            ]
        },
        {
            "country": "ANT",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 0.216
                },
                {
                    "year": 1851,
                    "value": 0.227
                },
                {
                    "year": 1852,
                    "value": 0.24
                },
                {
                    "year": 1853,
                    "value": 0.253
                },
                {
                    "year": 1854,
                    "value": 0.267
                },
                {
                    "year": 1855,
                    "value": 0.281
                },
                {
                    "year": 1856,
                    "value": 0.296
                },
                {
                    "year": 1857,
                    "value": 0.312
                },
                {
                    "year": 1858,
                    "value": 0.329
                },
                {
                    "year": 1859,
                    "value": 0.346
                },
                {
                    "year": 1860,
                    "value": 0.363
                },
                {
                    "year": 1861,
                    "value": 0.382
                },
                {
                    "year": 1862,
                    "value": 0.401
                },
                {
                    "year": 1863,
                    "value": 0.421
                },
                {
                    "year": 1864,
                    "value": 0.442
                },
                {
                    "year": 1865,
                    "value": 0.464
                },
                {
                    "year": 1866,
                    "value": 0.487
                },
                {
                    "year": 1867,
                    "value": 0.51
                },
                {
                    "year": 1868,
                    "value": 0.535
                },
                {
                    "year": 1869,
                    "value": 0.561
                },
                {
                    "year": 1870,
                    "value": 0.588
                },
                {
                    "year": 1871,
                    "value": 0.617
                },
                {
                    "year": 1872,
                    "value": 0.647
                },
                {
                    "year": 1873,
                    "value": 0.679
                },
                {
                    "year": 1874,
                    "value": 0.713
                },
                {
                    "year": 1875,
                    "value": 0.749
                },
                {
                    "year": 1876,
                    "value": 0.785
                },
                {
                    "year": 1877,
                    "value": 0.823
                },
                {
                    "year": 1878,
                    "value": 0.862
                },
                {
                    "year": 1879,
                    "value": 0.902
                },
                {
                    "year": 1880,
                    "value": 0.942
                },
                {
                    "year": 1881,
                    "value": 0.984
                },
                {
                    "year": 1882,
                    "value": 1.03
                },
                {
                    "year": 1883,
                    "value": 1.07
                },
                {
                    "year": 1884,
                    "value": 1.11
                },
                {
                    "year": 1885,
                    "value": 1.16
                },
                {
                    "year": 1886,
                    "value": 1.21
                },
                {
                    "year": 1887,
                    "value": 1.26
                },
                {
                    "year": 1888,
                    "value": 1.31
                },
                {
                    "year": 1889,
                    "value": 1.37
                },
                {
                    "year": 1890,
                    "value": 1.53
                },
                {
                    "year": 1891,
                    "value": 1.59
                },
                {
                    "year": 1892,
                    "value": 1.66
                },
                {
                    "year": 1893,
                    "value": 1.73
                },
                {
                    "year": 1894,
                    "value": 1.81
                },
                {
                    "year": 1895,
                    "value": 1.89
                },
                {
                    "year": 1896,
                    "value": 1.98
                },
                {
                    "year": 1897,
                    "value": 2.08
                },
                {
                    "year": 1898,
                    "value": 2.18
                },
                {
                    "year": 1899,
                    "value": 2.28
                },
                {
                    "year": 1900,
                    "value": 2.39
                },
                {
                    "year": 1901,
                    "value": 2.5
                },
                {
                    "year": 1902,
                    "value": 2.63
                },
                {
                    "year": 1903,
                    "value": 2.77
                },
                {
                    "year": 1904,
                    "value": 2.91
                },
                {
                    "year": 1905,
                    "value": 3.07
                },
                {
                    "year": 1906,
                    "value": 3.22
                },
                {
                    "year": 1907,
                    "value": 3.38
                },
                {
                    "year": 1908,
                    "value": 3.53
                },
                {
                    "year": 1909,
                    "value": 3.69
                },
                {
                    "year": 1910,
                    "value": 3.83
                },
                {
                    "year": 1911,
                    "value": 3.97
                },
                {
                    "year": 1912,
                    "value": 4.11
                },
                {
                    "year": 1913,
                    "value": 4.25
                },
                {
                    "year": 1914,
                    "value": 4.38
                },
                {
                    "year": 1915,
                    "value": 4.52
                },
                {
                    "year": 1916,
                    "value": 4.65
                },
                {
                    "year": 1917,
                    "value": 4.79
                },
                {
                    "year": 1918,
                    "value": 4.94
                },
                {
                    "year": 1919,
                    "value": 5.09
                },
                {
                    "year": 1920,
                    "value": 5.25
                },
                {
                    "year": 1921,
                    "value": 5.42
                },
                {
                    "year": 1922,
                    "value": 5.59
                },
                {
                    "year": 1923,
                    "value": 5.77
                },
                {
                    "year": 1924,
                    "value": 5.95
                },
                {
                    "year": 1925,
                    "value": 7.31
                },
                {
                    "year": 1926,
                    "value": 9.43
                },
                {
                    "year": 1927,
                    "value": 9.29
                },
                {
                    "year": 1928,
                    "value": 24.4
                },
                {
                    "year": 1929,
                    "value": 30.6
                },
                {
                    "year": 1930,
                    "value": 37.4
                },
                {
                    "year": 1931,
                    "value": 31.9
                },
                {
                    "year": 1932,
                    "value": 30.9
                },
                {
                    "year": 1933,
                    "value": 33.0
                },
                {
                    "year": 1934,
                    "value": 36.7
                },
                {
                    "year": 1935,
                    "value": 42.4
                },
                {
                    "year": 1936,
                    "value": 45.3
                },
                {
                    "year": 1937,
                    "value": 54.8
                },
                {
                    "year": 1938,
                    "value": 58.7
                },
                {
                    "year": 1939,
                    "value": 55.3
                },
                {
                    "year": 1940,
                    "value": 45.8
                },
                {
                    "year": 1941,
                    "value": 56.5
                },
                {
                    "year": 1942,
                    "value": 32.9
                },
                {
                    "year": 1943,
                    "value": 53.2
                },
                {
                    "year": 1944,
                    "value": 66.7
                },
                {
                    "year": 1945,
                    "value": 77.4
                },
                {
                    "year": 1946,
                    "value": 85.1
                },
                {
                    "year": 1947,
                    "value": 93.7
                },
                {
                    "year": 1948,
                    "value": 95.4
                },
                {
                    "year": 1949,
                    "value": 50.5
                },
                {
                    "year": 1950,
                    "value": 5.5
                },
                {
                    "year": 1951,
                    "value": 8.67
                },
                {
                    "year": 1952,
                    "value": 5.01
                },
                {
                    "year": 1953,
                    "value": 5.8
                },
                {
                    "year": 1954,
                    "value": 11.7
                },
                {
                    "year": 1955,
                    "value": 9.71
                },
                {
                    "year": 1956,
                    "value": 12.5
                },
                {
                    "year": 1957,
                    "value": 9.63
                },
                {
                    "year": 1958,
                    "value": 8.44
                },
                {
                    "year": 1959,
                    "value": 10.9
                },
                {
                    "year": 1960,
                    "value": 9.34
                },
                {
                    "year": 1961,
                    "value": 9.75
                },
                {
                    "year": 1962,
                    "value": 10.7
                },
                {
                    "year": 1963,
                    "value": 10.3
                },
                {
                    "year": 1964,
                    "value": 9.97
                },
                {
                    "year": 1965,
                    "value": 8.94
                },
                {
                    "year": 1966,
                    "value": 8.36
                },
                {
                    "year": 1967,
                    "value": 10.3
                },
                {
                    "year": 1968,
                    "value": 9.58
                },
                {
                    "year": 1969,
                    "value": 12.5
                },
                {
                    "year": 1970,
                    "value": 14.0
                },
                {
                    "year": 1971,
                    "value": 12.2
                },
                {
                    "year": 1972,
                    "value": 11.8
                },
                {
                    "year": 1973,
                    "value": 13.1
                },
                {
                    "year": 1974,
                    "value": 11.9
                },
                {
                    "year": 1975,
                    "value": 8.62
                },
                {
                    "year": 1976,
                    "value": 18.4
                },
                {
                    "year": 1977,
                    "value": 9.62
                },
                {
                    "year": 1978,
                    "value": 8.2
                },
                {
                    "year": 1979,
                    "value": 8.6
                },
                {
                    "year": 1980,
                    "value": 8.85
                },
                {
                    "year": 1981,
                    "value": 8.43
                },
                {
                    "year": 1982,
                    "value": 9.42
                },
                {
                    "year": 1983,
                    "value": 4.86
                },
                {
                    "year": 1984,
                    "value": 12.1
                },
                {
                    "year": 1985,
                    "value": 14.1
                },
                {
                    "year": 1986,
                    "value": 3.08
                },
                {
                    "year": 1987,
                    "value": 2.74
                },
                {
                    "year": 1988,
                    "value": 2.7
                },
                {
                    "year": 1989,
                    "value": 5.11
                },
                {
                    "year": 1990,
                    "value": 5.47
                },
                {
                    "year": 1991,
                    "value": 4.38
                },
                {
                    "year": 1992,
                    "value": 3.63
                },
                {
                    "year": 1993,
                    "value": 5.59
                },
                {
                    "year": 1994,
                    "value": 5.36
                },
                {
                    "year": 1995,
                    "value": 5.31
                },
                {
                    "year": 1996,
                    "value": 4.97
                },
                {
                    "year": 1997,
                    "value": 5.19
                },
                {
                    "year": 1998,
                    "value": 0.362
                },
                {
                    "year": 1999,
                    "value": 2.19
                },
                {
                    "year": 2000,
                    "value": 5.69
                },
                {
                    "year": 2001,
                    "value": 5.8
                },
                {
                    "year": 2002,
                    "value": 5.59
                },
                {
                    "year": 2003,
                    "value": 5.6
                },
                {
                    "year": 2004,
                    "value": 5.87
                },
                {
                    "year": 2005,
                    "value": 5.82
                },
                {
                    "year": 2006,
                    "value": 6.07
                },
                {
                    "year": 2007,
                    "value": 6.83
                },
                {
                    "year": 2008,
                    "value": 6.57
                },
                {
                    "year": 2009,
                    "value": 6.72
                },
                {
                    "year": 2010,
                    "value": 4.66
                },
                {
                    "year": 2011,
                    "value": 5.91
                },
                {
                    "year": 2012,
                    "value": 7.17
                },
                {
                    "year": 2013,
                    "value": 6.43
                },
                {
                    "year": 2014,
                    "value": 6.22
                }
            ]
        },
        {
            "country": "ARE",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 2.63e-05
                },
                {
                    "year": 1851,
                    "value": 2.77e-05
                },
                {
                    "year": 1852,
                    "value": 2.92e-05
                },
                {
                    "year": 1853,
                    "value": 3.08e-05
                },
                {
                    "year": 1854,
                    "value": 3.25e-05
                },
                {
                    "year": 1855,
                    "value": 3.43e-05
                },
                {
                    "year": 1856,
                    "value": 3.62e-05
                },
                {
                    "year": 1857,
                    "value": 3.81e-05
                },
                {
                    "year": 1858,
                    "value": 4.01e-05
                },
                {
                    "year": 1859,
                    "value": 4.22e-05
                },
                {
                    "year": 1860,
                    "value": 4.44e-05
                },
                {
                    "year": 1861,
                    "value": 4.66e-05
                },
                {
                    "year": 1862,
                    "value": 4.89e-05
                },
                {
                    "year": 1863,
                    "value": 5.14e-05
                },
                {
                    "year": 1864,
                    "value": 5.39e-05
                },
                {
                    "year": 1865,
                    "value": 5.66e-05
                },
                {
                    "year": 1866,
                    "value": 5.94e-05
                },
                {
                    "year": 1867,
                    "value": 6.23e-05
                },
                {
                    "year": 1868,
                    "value": 6.54e-05
                },
                {
                    "year": 1869,
                    "value": 6.85e-05
                },
                {
                    "year": 1870,
                    "value": 7.18e-05
                },
                {
                    "year": 1871,
                    "value": 7.53e-05
                },
                {
                    "year": 1872,
                    "value": 7.9e-05
                },
                {
                    "year": 1873,
                    "value": 8.3e-05
                },
                {
                    "year": 1874,
                    "value": 8.71e-05
                },
                {
                    "year": 1875,
                    "value": 9.14e-05
                },
                {
                    "year": 1876,
                    "value": 9.59e-05
                },
                {
                    "year": 1877,
                    "value": 0.000101
                },
                {
                    "year": 1878,
                    "value": 0.000105
                },
                {
                    "year": 1879,
                    "value": 0.00011
                },
                {
                    "year": 1880,
                    "value": 0.000115
                },
                {
                    "year": 1881,
                    "value": 0.00012
                },
                {
                    "year": 1882,
                    "value": 0.000125
                },
                {
                    "year": 1883,
                    "value": 0.000131
                },
                {
                    "year": 1884,
                    "value": 0.000136
                },
                {
                    "year": 1885,
                    "value": 0.000142
                },
                {
                    "year": 1886,
                    "value": 0.000148
                },
                {
                    "year": 1887,
                    "value": 0.000154
                },
                {
                    "year": 1888,
                    "value": 0.00016
                },
                {
                    "year": 1889,
                    "value": 0.000167
                },
                {
                    "year": 1890,
                    "value": 0.000189
                },
                {
                    "year": 1891,
                    "value": 0.000197
                },
                {
                    "year": 1892,
                    "value": 0.000206
                },
                {
                    "year": 1893,
                    "value": 0.000216
                },
                {
                    "year": 1894,
                    "value": 0.000227
                },
                {
                    "year": 1895,
                    "value": 0.000238
                },
                {
                    "year": 1896,
                    "value": 0.00025
                },
                {
                    "year": 1897,
                    "value": 0.000263
                },
                {
                    "year": 1898,
                    "value": 0.000277
                },
                {
                    "year": 1899,
                    "value": 0.000291
                },
                {
                    "year": 1900,
                    "value": 0.000305
                },
                {
                    "year": 1901,
                    "value": 0.000321
                },
                {
                    "year": 1902,
                    "value": 0.000338
                },
                {
                    "year": 1903,
                    "value": 0.000356
                },
                {
                    "year": 1904,
                    "value": 0.000376
                },
                {
                    "year": 1905,
                    "value": 0.000397
                },
                {
                    "year": 1906,
                    "value": 0.000418
                },
                {
                    "year": 1907,
                    "value": 0.00044
                },
                {
                    "year": 1908,
                    "value": 0.000462
                },
                {
                    "year": 1909,
                    "value": 0.000484
                },
                {
                    "year": 1910,
                    "value": 0.000506
                },
                {
                    "year": 1911,
                    "value": 0.00053
                },
                {
                    "year": 1912,
                    "value": 0.000556
                },
                {
                    "year": 1913,
                    "value": 0.000584
                },
                {
                    "year": 1914,
                    "value": 0.000613
                },
                {
                    "year": 1915,
                    "value": 0.000641
                },
                {
                    "year": 1916,
                    "value": 0.000669
                },
                {
                    "year": 1917,
                    "value": 0.000694
                },
                {
                    "year": 1918,
                    "value": 0.000715
                },
                {
                    "year": 1919,
                    "value": 0.000732
                },
                {
                    "year": 1920,
                    "value": 0.000744
                },
                {
                    "year": 1921,
                    "value": 0.000752
                },
                {
                    "year": 1922,
                    "value": 0.000757
                },
                {
                    "year": 1923,
                    "value": 0.000762
                },
                {
                    "year": 1924,
                    "value": 0.000765
                },
                {
                    "year": 1925,
                    "value": 0.000769
                },
                {
                    "year": 1926,
                    "value": 0.000772
                },
                {
                    "year": 1927,
                    "value": 0.000776
                },
                {
                    "year": 1928,
                    "value": 0.000781
                },
                {
                    "year": 1929,
                    "value": 0.000788
                },
                {
                    "year": 1930,
                    "value": 0.000797
                },
                {
                    "year": 1931,
                    "value": 0.000863
                },
                {
                    "year": 1932,
                    "value": 0.00102
                },
                {
                    "year": 1933,
                    "value": 0.00126
                },
                {
                    "year": 1934,
                    "value": 0.00156
                },
                {
                    "year": 1935,
                    "value": 0.00189
                },
                {
                    "year": 1936,
                    "value": 0.00224
                },
                {
                    "year": 1937,
                    "value": 0.0026
                },
                {
                    "year": 1938,
                    "value": 0.00292
                },
                {
                    "year": 1939,
                    "value": 0.00321
                },
                {
                    "year": 1940,
                    "value": 0.00344
                },
                {
                    "year": 1941,
                    "value": 0.00362
                },
                {
                    "year": 1942,
                    "value": 0.00376
                },
                {
                    "year": 1943,
                    "value": 0.00389
                },
                {
                    "year": 1944,
                    "value": 0.004
                },
                {
                    "year": 1945,
                    "value": 0.00412
                },
                {
                    "year": 1946,
                    "value": 0.00424
                },
                {
                    "year": 1947,
                    "value": 0.00437
                },
                {
                    "year": 1948,
                    "value": 0.00453
                },
                {
                    "year": 1949,
                    "value": 0.00472
                },
                {
                    "year": 1950,
                    "value": 0.00495
                },
                {
                    "year": 1951,
                    "value": 0.00528
                },
                {
                    "year": 1952,
                    "value": 0.00577
                },
                {
                    "year": 1953,
                    "value": 0.0064
                },
                {
                    "year": 1954,
                    "value": 0.00714
                },
                {
                    "year": 1955,
                    "value": 0.00798
                },
                {
                    "year": 1956,
                    "value": 0.00889
                },
                {
                    "year": 1957,
                    "value": 0.00987
                },
                {
                    "year": 1958,
                    "value": 0.0109
                },
                {
                    "year": 1959,
                    "value": 0.00952
                },
                {
                    "year": 1960,
                    "value": 0.00952
                },
                {
                    "year": 1961,
                    "value": 0.00952
                },
                {
                    "year": 1962,
                    "value": 0.0159
                },
                {
                    "year": 1963,
                    "value": 0.019
                },
                {
                    "year": 1964,
                    "value": 0.0159
                },
                {
                    "year": 1965,
                    "value": 0.019
                },
                {
                    "year": 1966,
                    "value": 0.0222
                },
                {
                    "year": 1967,
                    "value": 0.796
                },
                {
                    "year": 1968,
                    "value": 1.08
                },
                {
                    "year": 1969,
                    "value": 20.4
                },
                {
                    "year": 1970,
                    "value": 15.1
                },
                {
                    "year": 1971,
                    "value": 21.0
                },
                {
                    "year": 1972,
                    "value": 23.2
                },
                {
                    "year": 1973,
                    "value": 30.3
                },
                {
                    "year": 1974,
                    "value": 30.9
                },
                {
                    "year": 1975,
                    "value": 30.5
                },
                {
                    "year": 1976,
                    "value": 38.8
                },
                {
                    "year": 1977,
                    "value": 37.6
                },
                {
                    "year": 1978,
                    "value": 43.3
                },
                {
                    "year": 1979,
                    "value": 34.1
                },
                {
                    "year": 1980,
                    "value": 34.2
                },
                {
                    "year": 1981,
                    "value": 33.2
                },
                {
                    "year": 1982,
                    "value": 32.9
                },
                {
                    "year": 1983,
                    "value": 31.6
                },
                {
                    "year": 1984,
                    "value": 42.9
                },
                {
                    "year": 1985,
                    "value": 45.0
                },
                {
                    "year": 1986,
                    "value": 42.0
                },
                {
                    "year": 1987,
                    "value": 42.1
                },
                {
                    "year": 1988,
                    "value": 42.2
                },
                {
                    "year": 1989,
                    "value": 47.6
                },
                {
                    "year": 1990,
                    "value": 45.8
                },
                {
                    "year": 1991,
                    "value": 49.1
                },
                {
                    "year": 1992,
                    "value": 50.2
                },
                {
                    "year": 1993,
                    "value": 56.9
                },
                {
                    "year": 1994,
                    "value": 63.3
                },
                {
                    "year": 1995,
                    "value": 69.8
                },
                {
                    "year": 1996,
                    "value": 76.4
                },
                {
                    "year": 1997,
                    "value": 85.0
                },
                {
                    "year": 1998,
                    "value": 91.5
                },
                {
                    "year": 1999,
                    "value": 97.6
                },
                {
                    "year": 2000,
                    "value": 104.0
                },
                {
                    "year": 2001,
                    "value": 111.0
                },
                {
                    "year": 2002,
                    "value": 118.0
                },
                {
                    "year": 2003,
                    "value": 125.0
                },
                {
                    "year": 2004,
                    "value": 132.0
                },
                {
                    "year": 2005,
                    "value": 139.0
                },
                {
                    "year": 2006,
                    "value": 149.0
                },
                {
                    "year": 2007,
                    "value": 163.0
                },
                {
                    "year": 2008,
                    "value": 189.0
                },
                {
                    "year": 2009,
                    "value": 201.0
                },
                {
                    "year": 2010,
                    "value": 193.0
                },
                {
                    "year": 2011,
                    "value": 191.0
                },
                {
                    "year": 2012,
                    "value": 207.0
                },
                {
                    "year": 2013,
                    "value": 203.0
                },
                {
                    "year": 2014,
                    "value": 215.0
                }
            ]
        },
        {
            "country": "ARG",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": -1.82
                },
                {
                    "year": 1851,
                    "value": -1.86
                },
                {
                    "year": 1852,
                    "value": -1.89
                },
                {
                    "year": 1853,
                    "value": -1.91
                },
                {
                    "year": 1854,
                    "value": -1.93
                },
                {
                    "year": 1855,
                    "value": -1.95
                },
                {
                    "year": 1856,
                    "value": -1.96
                },
                {
                    "year": 1857,
                    "value": -1.97
                },
                {
                    "year": 1858,
                    "value": -1.98
                },
                {
                    "year": 1859,
                    "value": -1.99
                },
                {
                    "year": 1860,
                    "value": -2.04
                },
                {
                    "year": 1861,
                    "value": -1.92
                },
                {
                    "year": 1862,
                    "value": -1.88
                },
                {
                    "year": 1863,
                    "value": -1.85
                },
                {
                    "year": 1864,
                    "value": -1.83
                },
                {
                    "year": 1865,
                    "value": -1.81
                },
                {
                    "year": 1866,
                    "value": -1.85
                },
                {
                    "year": 1867,
                    "value": -1.89
                },
                {
                    "year": 1868,
                    "value": -1.92
                },
                {
                    "year": 1869,
                    "value": -1.96
                },
                {
                    "year": 1870,
                    "value": -1.94
                },
                {
                    "year": 1871,
                    "value": -1.93
                },
                {
                    "year": 1872,
                    "value": -1.93
                },
                {
                    "year": 1873,
                    "value": -1.92
                },
                {
                    "year": 1874,
                    "value": -1.91
                },
                {
                    "year": 1875,
                    "value": -1.89
                },
                {
                    "year": 1876,
                    "value": -1.86
                },
                {
                    "year": 1877,
                    "value": -1.77
                },
                {
                    "year": 1878,
                    "value": -1.7
                },
                {
                    "year": 1879,
                    "value": -1.62
                },
                {
                    "year": 1880,
                    "value": -1.54
                },
                {
                    "year": 1881,
                    "value": 2.49
                },
                {
                    "year": 1882,
                    "value": 3.63
                },
                {
                    "year": 1883,
                    "value": 4.56
                },
                {
                    "year": 1884,
                    "value": 5.33
                },
                {
                    "year": 1885,
                    "value": 5.99
                },
                {
                    "year": 1886,
                    "value": 6.58
                },
                {
                    "year": 1887,
                    "value": 6.87
                },
                {
                    "year": 1888,
                    "value": 6.91
                },
                {
                    "year": 1889,
                    "value": 7.86
                },
                {
                    "year": 1890,
                    "value": 7.67
                },
                {
                    "year": 1891,
                    "value": 5.15
                },
                {
                    "year": 1892,
                    "value": 5.09
                },
                {
                    "year": 1893,
                    "value": 4.9
                },
                {
                    "year": 1894,
                    "value": 5.02
                },
                {
                    "year": 1895,
                    "value": 5.05
                },
                {
                    "year": 1896,
                    "value": 4.95
                },
                {
                    "year": 1897,
                    "value": 4.66
                },
                {
                    "year": 1898,
                    "value": 4.8
                },
                {
                    "year": 1899,
                    "value": 5.23
                },
                {
                    "year": 1900,
                    "value": 4.46
                },
                {
                    "year": 1901,
                    "value": 12.5
                },
                {
                    "year": 1902,
                    "value": 15.0
                },
                {
                    "year": 1903,
                    "value": 16.9
                },
                {
                    "year": 1904,
                    "value": 19.2
                },
                {
                    "year": 1905,
                    "value": 20.6
                },
                {
                    "year": 1906,
                    "value": 23.1
                },
                {
                    "year": 1907,
                    "value": 23.6
                },
                {
                    "year": 1908,
                    "value": 25.2
                },
                {
                    "year": 1909,
                    "value": 24.1
                },
                {
                    "year": 1910,
                    "value": 26.9
                },
                {
                    "year": 1911,
                    "value": 20.0
                },
                {
                    "year": 1912,
                    "value": 17.3
                },
                {
                    "year": 1913,
                    "value": 16.1
                },
                {
                    "year": 1914,
                    "value": 13.2
                },
                {
                    "year": 1915,
                    "value": 10.4
                },
                {
                    "year": 1916,
                    "value": 8.22
                },
                {
                    "year": 1917,
                    "value": 5.47
                },
                {
                    "year": 1918,
                    "value": 5.37
                },
                {
                    "year": 1919,
                    "value": 6.11
                },
                {
                    "year": 1920,
                    "value": 7.69
                },
                {
                    "year": 1921,
                    "value": 13.0
                },
                {
                    "year": 1922,
                    "value": 16.1
                },
                {
                    "year": 1923,
                    "value": 18.3
                },
                {
                    "year": 1924,
                    "value": 21.5
                },
                {
                    "year": 1925,
                    "value": 22.7
                },
                {
                    "year": 1926,
                    "value": 23.0
                },
                {
                    "year": 1927,
                    "value": 25.0
                },
                {
                    "year": 1928,
                    "value": 24.6
                },
                {
                    "year": 1929,
                    "value": 25.1
                },
                {
                    "year": 1930,
                    "value": 25.0
                },
                {
                    "year": 1931,
                    "value": 26.5
                },
                {
                    "year": 1932,
                    "value": 27.2
                },
                {
                    "year": 1933,
                    "value": 27.6
                },
                {
                    "year": 1934,
                    "value": 28.7
                },
                {
                    "year": 1935,
                    "value": 28.7
                },
                {
                    "year": 1936,
                    "value": 29.9
                },
                {
                    "year": 1937,
                    "value": 31.6
                },
                {
                    "year": 1938,
                    "value": 31.5
                },
                {
                    "year": 1939,
                    "value": 32.6
                },
                {
                    "year": 1940,
                    "value": 31.5
                },
                {
                    "year": 1941,
                    "value": 29.7
                },
                {
                    "year": 1942,
                    "value": 29.3
                },
                {
                    "year": 1943,
                    "value": 29.8
                },
                {
                    "year": 1944,
                    "value": 29.7
                },
                {
                    "year": 1945,
                    "value": 29.5
                },
                {
                    "year": 1946,
                    "value": 29.9
                },
                {
                    "year": 1947,
                    "value": 31.1
                },
                {
                    "year": 1948,
                    "value": 34.0
                },
                {
                    "year": 1949,
                    "value": 32.8
                },
                {
                    "year": 1950,
                    "value": 45.7
                },
                {
                    "year": 1951,
                    "value": 57.4
                },
                {
                    "year": 1952,
                    "value": 60.8
                },
                {
                    "year": 1953,
                    "value": 62.0
                },
                {
                    "year": 1954,
                    "value": 65.1
                },
                {
                    "year": 1955,
                    "value": 68.9
                },
                {
                    "year": 1956,
                    "value": 73.9
                },
                {
                    "year": 1957,
                    "value": 77.6
                },
                {
                    "year": 1958,
                    "value": 75.3
                },
                {
                    "year": 1959,
                    "value": 80.0
                },
                {
                    "year": 1960,
                    "value": 80.4
                },
                {
                    "year": 1961,
                    "value": 97.0
                },
                {
                    "year": 1962,
                    "value": 104.0
                },
                {
                    "year": 1963,
                    "value": 104.0
                },
                {
                    "year": 1964,
                    "value": 112.0
                },
                {
                    "year": 1965,
                    "value": 117.0
                },
                {
                    "year": 1966,
                    "value": 123.0
                },
                {
                    "year": 1967,
                    "value": 126.0
                },
                {
                    "year": 1968,
                    "value": 130.0
                },
                {
                    "year": 1969,
                    "value": 138.0
                },
                {
                    "year": 1970,
                    "value": 143.0
                },
                {
                    "year": 1971,
                    "value": 141.0
                },
                {
                    "year": 1972,
                    "value": 141.0
                },
                {
                    "year": 1973,
                    "value": 143.0
                },
                {
                    "year": 1974,
                    "value": 144.0
                },
                {
                    "year": 1975,
                    "value": 142.0
                },
                {
                    "year": 1976,
                    "value": 147.0
                },
                {
                    "year": 1977,
                    "value": 148.0
                },
                {
                    "year": 1978,
                    "value": 150.0
                },
                {
                    "year": 1979,
                    "value": 157.0
                },
                {
                    "year": 1980,
                    "value": 156.0
                },
                {
                    "year": 1981,
                    "value": 150.0
                },
                {
                    "year": 1982,
                    "value": 178.0
                },
                {
                    "year": 1983,
                    "value": 187.0
                },
                {
                    "year": 1984,
                    "value": 194.0
                },
                {
                    "year": 1985,
                    "value": 194.0
                },
                {
                    "year": 1986,
                    "value": 202.0
                },
                {
                    "year": 1987,
                    "value": 214.0
                },
                {
                    "year": 1988,
                    "value": 220.0
                },
                {
                    "year": 1989,
                    "value": 218.0
                },
                {
                    "year": 1990,
                    "value": 216.0
                },
                {
                    "year": 1991,
                    "value": 219.0
                },
                {
                    "year": 1992,
                    "value": 207.0
                },
                {
                    "year": 1993,
                    "value": 206.0
                },
                {
                    "year": 1994,
                    "value": 207.0
                },
                {
                    "year": 1995,
                    "value": 206.0
                },
                {
                    "year": 1996,
                    "value": 207.0
                },
                {
                    "year": 1997,
                    "value": 208.0
                },
                {
                    "year": 1998,
                    "value": 207.0
                },
                {
                    "year": 1999,
                    "value": 206.0
                },
                {
                    "year": 2000,
                    "value": 207.0
                },
                {
                    "year": 2001,
                    "value": 196.0
                },
                {
                    "year": 2002,
                    "value": 186.0
                },
                {
                    "year": 2003,
                    "value": 194.0
                },
                {
                    "year": 2004,
                    "value": 213.0
                },
                {
                    "year": 2005,
                    "value": 216.0
                },
                {
                    "year": 2006,
                    "value": 263.0
                },
                {
                    "year": 2007,
                    "value": 255.0
                },
                {
                    "year": 2008,
                    "value": 272.0
                },
                {
                    "year": 2009,
                    "value": 263.0
                },
                {
                    "year": 2010,
                    "value": 263.0
                },
                {
                    "year": 2011,
                    "value": 263.0
                },
                {
                    "year": 2012,
                    "value": 267.0
                },
                {
                    "year": 2013,
                    "value": 262.0
                },
                {
                    "year": 2014,
                    "value": 263.0
                }
            ]
        },
        {
            "country": "ARM",
            "sector": "Total including LULUCF",
            "parentSector": "",
            "valuesPerYear": [
                {
                    "year": 1850,
                    "value": 1.2
                },
                {
                    "year": 1851,
                    "value": 1.2
                },
                {
                    "year": 1852,
                    "value": 1.21
                },
                {
                    "year": 1853,
                    "value": 1.21
                },
                {
                    "year": 1854,
                    "value": 1.22
                },
                {
                    "year": 1855,
                    "value": 1.22
                },
                {
                    "year": 1856,
                    "value": 1.23
                },
                {
                    "year": 1857,
                    "value": 1.23
                },
                {
                    "year": 1858,
                    "value": 1.24
                },
                {
                    "year": 1859,
                    "value": 1.25
                },
                {
                    "year": 1860,
                    "value": 1.25
                },
                {
                    "year": 1861,
                    "value": 1.26
                },
                {
                    "year": 1862,
                    "value": 1.13
                },
                {
                    "year": 1863,
                    "value": 1.13
                },
                {
                    "year": 1864,
                    "value": 1.13
                },
                {
                    "year": 1865,
                    "value": 1.13
                },
                {
                    "year": 1866,
                    "value": 1.13
                },
                {
                    "year": 1867,
                    "value": 1.13
                },
                {
                    "year": 1868,
                    "value": 1.13
                },
                {
                    "year": 1869,
                    "value": 1.12
                },
                {
                    "year": 1870,
                    "value": 1.12
                },
                {
                    "year": 1871,
                    "value": 1.12
                },
                {
                    "year": 1872,
                    "value": 1.13
                },
                {
                    "year": 1873,
                    "value": 1.13
                },
                {
                    "year": 1874,
                    "value": 1.14
                },
                {
                    "year": 1875,
                    "value": 1.14
                },
                {
                    "year": 1876,
                    "value": 1.15
                },
                {
                    "year": 1877,
                    "value": 1.15
                },
                {
                    "year": 1878,
                    "value": 1.16
                },
                {
                    "year": 1879,
                    "value": 1.16
                },
                {
                    "year": 1880,
                    "value": 1.16
                },
                {
                    "year": 1881,
                    "value": 1.17
                },
                {
                    "year": 1882,
                    "value": 1.17
                },
                {
                    "year": 1883,
                    "value": 1.17
                },
                {
                    "year": 1884,
                    "value": 1.18
                },
                {
                    "year": 1885,
                    "value": 1.19
                },
                {
                    "year": 1886,
                    "value": 1.19
                },
                {
                    "year": 1887,
                    "value": 1.2
                },
                {
                    "year": 1888,
                    "value": 1.2
                },
                {
                    "year": 1889,
                    "value": 1.2
                },
                {
                    "year": 1890,
                    "value": 1.21
                },
                {
                    "year": 1891,
                    "value": 1.22
                },
                {
                    "year": 1892,
                    "value": 1.23
                },
                {
                    "year": 1893,
                    "value": 1.24
                },
                {
                    "year": 1894,
                    "value": 1.24
                },
                {
                    "year": 1895,
                    "value": 1.26
                },
                {
                    "year": 1896,
                    "value": 1.26
                },
                {
                    "year": 1897,
                    "value": 1.27
                },
                {
                    "year": 1898,
                    "value": 1.28
                },
                {
                    "year": 1899,
                    "value": 1.29
                },
                {
                    "year": 1900,
                    "value": 1.31
                },
                {
                    "year": 1901,
                    "value": 1.33
                },
                {
                    "year": 1902,
                    "value": 1.32
                },
                {
                    "year": 1903,
                    "value": 1.31
                },
                {
                    "year": 1904,
                    "value": 1.32
                },
                {
                    "year": 1905,
                    "value": 1.29
                },
                {
                    "year": 1906,
                    "value": 1.31
                },
                {
                    "year": 1907,
                    "value": 1.32
                },
                {
                    "year": 1908,
                    "value": 1.32
                },
                {
                    "year": 1909,
                    "value": 1.32
                },
                {
                    "year": 1910,
                    "value": 1.33
                },
                {
                    "year": 1911,
                    "value": 1.32
                },
                {
                    "year": 1912,
                    "value": 1.33
                },
                {
                    "year": 1913,
                    "value": 1.41
                },
                {
                    "year": 1914,
                    "value": 1.43
                },
                {
                    "year": 1915,
                    "value": 1.46
                },
                {
                    "year": 1916,
                    "value": 1.49
                },
                {
                    "year": 1917,
                    "value": 1.49
                },
                {
                    "year": 1918,
                    "value": 1.44
                },
                {
                    "year": 1919,
                    "value": 1.46
                },
                {
                    "year": 1920,
                    "value": 1.47
                },
                {
                    "year": 1921,
                    "value": 1.49
                },
                {
                    "year": 1922,
                    "value": 1.53
                },
                {
                    "year": 1923,
                    "value": 1.55
                },
                {
                    "year": 1924,
                    "value": 1.58
                },
                {
                    "year": 1925,
                    "value": 1.61
                },
                {
                    "year": 1926,
                    "value": 1.65
                },
                {
                    "year": 1927,
                    "value": 1.69
                },
                {
                    "year": 1928,
                    "value": 1.71
                },
                {
                    "year": 1929,
                    "value": 1.74
                },
                {
                    "year": 1930,
                    "value": 1.86
                },
                {
                    "year": 1931,
                    "value": 1.93
                },
                {
                    "year": 1932,
                    "value": 1.93
                },
                {
                    "year": 1933,
                    "value": 1.95
                },
                {
                    "year": 1934,
                    "value": 1.98
                },
                {
                    "year": 1935,
                    "value": 1.99
                },
                {
                    "year": 1936,
                    "value": 2.01
                },
                {
                    "year": 1937,
                    "value": 1.99
                },
                {
                    "year": 1938,
                    "value": 1.99
                },
                {
                    "year": 1939,
                    "value": 1.96
                },
                {
                    "year": 1940,
                    "value": 1.96
                },
                {
                    "year": 1941,
                    "value": 1.67
                },
                {
                    "year": 1942,
                    "value": 1.48
                },
                {
                    "year": 1943,
                    "value": 1.37
                },
                {
                    "year": 1944,
                    "value": 1.37
                },
                {
                    "year": 1945,
                    "value": 1.12
                },
                {
                    "year": 1946,
                    "value": 1.12
                },
                {
                    "year": 1947,
                    "value": 1.16
                },
                {
                    "year": 1948,
                    "value": 1.17
                },
                {
                    "year": 1949,
                    "value": 1.21
                },
                {
                    "year": 1950,
                    "value": 1.29
                },
                {
                    "year": 1951,
                    "value": 3.08
                },
                {
                    "year": 1952,
                    "value": 3.51
                },
                {
                    "year": 1953,
                    "value": 3.92
                },
                {
                    "year": 1954,
                    "value": 4.36
                },
                {
                    "year": 1955,
                    "value": 4.86
                },
                {
                    "year": 1956,
                    "value": 5.4
                },
                {
                    "year": 1957,
                    "value": 5.98
                },
                {
                    "year": 1958,
                    "value": 6.58
                },
                {
                    "year": 1959,
                    "value": 5.74
                },
                {
                    "year": 1960,
                    "value": 6.06
                },
                {
                    "year": 1961,
                    "value": 6.28
                },
                {
                    "year": 1962,
                    "value": 6.62
                },
                {
                    "year": 1963,
                    "value": 6.97
                },
                {
                    "year": 1964,
                    "value": 7.34
                },
                {
                    "year": 1965,
                    "value": 7.69
                },
                {
                    "year": 1966,
                    "value": 7.88
                },
                {
                    "year": 1967,
                    "value": 8.11
                },
                {
                    "year": 1968,
                    "value": 8.27
                },
                {
                    "year": 1969,
                    "value": 8.48
                },
                {
                    "year": 1970,
                    "value": 8.1
                },
                {
                    "year": 1971,
                    "value": 8.38
                },
                {
                    "year": 1972,
                    "value": 8.59
                },
                {
                    "year": 1973,
                    "value": 8.8
                },
                {
                    "year": 1974,
                    "value": 9.16
                },
                {
                    "year": 1975,
                    "value": 9.59
                },
                {
                    "year": 1976,
                    "value": 9.96
                },
                {
                    "year": 1977,
                    "value": 10.3
                },
                {
                    "year": 1978,
                    "value": 10.7
                },
                {
                    "year": 1979,
                    "value": 10.8
                },
                {
                    "year": 1980,
                    "value": 11.1
                },
                {
                    "year": 1981,
                    "value": 11.4
                },
                {
                    "year": 1982,
                    "value": 11.6
                },
                {
                    "year": 1983,
                    "value": 11.9
                },
                {
                    "year": 1984,
                    "value": 12.2
                },
                {
                    "year": 1985,
                    "value": 12.8
                },
                {
                    "year": 1986,
                    "value": 12.6
                },
                {
                    "year": 1987,
                    "value": 13.5
                },
                {
                    "year": 1988,
                    "value": 13.9
                },
                {
                    "year": 1989,
                    "value": 13.8
                },
                {
                    "year": 1990,
                    "value": 22.5
                },
                {
                    "year": 1991,
                    "value": 20.2
                },
                {
                    "year": 1992,
                    "value": 18.3
                },
                {
                    "year": 1993,
                    "value": 16.5
                },
                {
                    "year": 1994,
                    "value": 14.6
                },
                {
                    "year": 1995,
                    "value": 12.7
                },
                {
                    "year": 1996,
                    "value": 10.9
                },
                {
                    "year": 1997,
                    "value": 9.05
                },
                {
                    "year": 1998,
                    "value": 7.21
                },
                {
                    "year": 1999,
                    "value": 5.36
                },
                {
                    "year": 2000,
                    "value": 3.52
                },
                {
                    "year": 2001,
                    "value": 3.67
                },
                {
                    "year": 2002,
                    "value": 3.83
                },
                {
                    "year": 2003,
                    "value": 3.99
                },
                {
                    "year": 2004,
                    "value": 4.18
                },
                {
                    "year": 2005,
                    "value": 4.34
                },
                {
                    "year": 2006,
                    "value": 4.52
                },
                {
                    "year": 2007,
                    "value": 4.6
                },
                {
                    "year": 2008,
                    "value": 4.68
                },
                {
                    "year": 2009,
                    "value": 4.75
                },
                {
                    "year": 2010,
                    "value": 4.83
                },
                {
                    "year": 2011,
                    "value": 5.3
                },
                {
                    "year": 2012,
                    "value": 6.13
                },
                {
                    "year": 2013,
                    "value": 5.92
                },
                {
                    "year": 2014,
                    "value": 6.4
                }
            ]
        }
    ]
