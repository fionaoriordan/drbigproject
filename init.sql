USE datarepresentation;

CREATE TABLE toys(
    id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    maker VARCHAR(250) NOT NULL,
    model VARCHAR(20) NOT NULL,
    colour VARCHAR(20) DEFAULT NULL,
    quantity int
    );

CREATE TABLE dispatches(
    dispatch_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(250) NOT NULL,
    address VARCHAR(250) NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (dispatch_id),
    CONSTRAINT FK_toys
    FOREIGN KEY (product_id)
    REFERENCES toys(id)
    ON DELETE RESTRICT
    );   

-- test insert
-- insert into dispatches(name,address,product_id) values('Finn', 'Galway', 1);
-- test delete (should not allow)
-- delete from toys where id = 1;