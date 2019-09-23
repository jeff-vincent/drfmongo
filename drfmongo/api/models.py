from django.db import models

class Property(Base):

    id = Column(Integer, primary_key=True)
    x = Column(String(50))
    y = Column(String(50))
    pams_pin = Column(String(50)) 
    municipal_code = Column(String(50))
    block = Column(String(50))
    lot = Column(String(100))
    qualifier = Column(String(50))
    prop_class = Column(String(50))
    county = Column(String(50))
    municipal_name = Column(String(100))
    property_location = Column(String(50))
    owner_name = Column(String(50))
    owner_st_address = Column(String(50)) 
    owner_city_state = Column(String(100))
    owner_zip_code = Column(String(50))
    land_val = Column(String(100))
    imprvt_val = Column(String(50))
    net_value = Column(String(50))
    last_yr_tx = Column(String(50))
    bldg_desc = Column(String(1100))
    land_desc = Column(String(1100))
    calc_acre = Column(String(100))
    add_lots1 = Column(String(100))
    add_lots2 = Column(String(100))
    fac_name = Column(String(100))
    prop_use = Column(String(100))
    bldg_class = Column(String(100))
    deed_book = Column(String(100))
    deed_page = Column(String(100))
    deed_date = Column(String(100))
    yr_constr = Column(String(100))
    sales_code = Column(String(100))
    sale_price = Column(String(100))
    dwell = Column(String(100))
    comm_dwell = Column(String(100))
    latitude = Column(String(100))
    longitude = Column(String(100))
    accuracy_score = Column(String(100))
    accuracy_type = Column(String(100))
    number = Column(String(100))
    property_street = Column(String(100))
    street = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    zipcode = Column(String(100))
    county = Column(String(100))
    source = Column(String(100))
    summary = Column(String(10000))
    delivery_line_1 = Column(String(100))
    delivery_line_2 = Column(String(100))
    city_name = Column(String(100))
    state_abbreviation = Column(String(100))
    full_zipcode = Column(String(100))
    notes = Column(String(100))
    county_name = Column(String(100))
    rdi = Column(String(100))
    precision = Column(String(100))
    dpv_match_code = Column(String(100))
    dpv_footnotes = Column(String(100))
    footnotes = Column(String(100))
    zip_type = Column(String(100))
    carrier_route = Column(String(100))
    dpv_vacant = Column(String(100))
    active = Column(String(100))
    urbanization = Column(String(100))

    def __repr__(self):
        return '<Property %r>' % self.id