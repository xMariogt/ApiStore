-- -----------------------------------------------------
-- Schema STORE_TEST
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `STORE_TEST`;
-- -----------------------------------------------------
-- Schema STORE_TEST
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `STORE_TEST` DEFAULT CHARACTER SET utf8 ;
USE `STORE_TEST` ;

-- -----------------------------------------------------
-- Table `STORE_TEST`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `STORE_TEST`.`USUARIO` (
  `IDUSUARIO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(200) NOT NULL,
  `APELLIDO` VARCHAR(200) NOT NULL,
  `EDAD` TINYINT(2) NOT NULL,
  `CORREO` VARCHAR(45) NOT NULL,
  `PASSWORD` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`IDUSUARIO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `STORE_TEST`.`METODO_PAGO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `STORE_TEST`.`METODO_PAGO` (
  `IDMETODO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`IDMETODO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `STORE_TEST`.`CATEGORIA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `STORE_TEST`.`CATEGORIA` (
  `IDCATEGORIA` INT NOT NULL,
  `NOMBRE` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`IDCATEGORIA`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `STORE_TEST`.`PRODUCTO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `STORE_TEST`.`PRODUCTO` (
  `IDPRODUCTO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(200) NOT NULL,
  `DESCRIPCION` VARCHAR(200) NOT NULL,
  `PRECIO` FLOAT NOT NULL,
  `STOCK` INT NOT NULL,
  `IDCATEGORIA` INT NOT NULL,
  PRIMARY KEY (`IDPRODUCTO`),
  INDEX `fk_PRODUCTO_CATEGORIA_idx` (`IDCATEGORIA` ASC) VISIBLE,
  CONSTRAINT `fk_PRODUCTO_CATEGORIA`
    FOREIGN KEY (`IDCATEGORIA`)
    REFERENCES `STORE_TEST`.`CATEGORIA` (`IDCATEGORIA`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `STORE_TEST`.`PEDIDO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `STORE_TEST`.`PEDIDO` (
  `IDPEDIDO` INT NOT NULL AUTO_INCREMENT,
  `FECHA_PEDIDO` DATETIME NOT NULL,
  `TOTAL` FLOAT NOT NULL,
  `CANTIDAD` INT NOT NULL,
  `IDMETODO` INT NOT NULL,
  `IDPRODUCTO` INT NOT NULL,
  `IDUSUARIO` INT NOT NULL,
  PRIMARY KEY (`IDPEDIDO`),
  INDEX `fk_PEDIDO_METODO_PAGO1_idx` (`IDMETODO` ASC) VISIBLE,
  INDEX `fk_PEDIDO_PRODUCTO1_idx` (`IDPRODUCTO` ASC) VISIBLE,
  INDEX `fk_PEDIDO_USUARIO1_idx` (`IDUSUARIO` ASC) VISIBLE,
  CONSTRAINT `fk_PEDIDO_METODO_PAGO1`
    FOREIGN KEY (`IDMETODO`)
    REFERENCES `STORE_TEST`.`METODO_PAGO` (`IDMETODO`),
  CONSTRAINT `fk_PEDIDO_PRODUCTO1`
    FOREIGN KEY (`IDPRODUCTO`)
    REFERENCES `STORE_TEST`.`PRODUCTO` (`IDPRODUCTO`),
  CONSTRAINT `fk_PEDIDO_USUARIO1`
    FOREIGN KEY (`IDUSUARIO`)
    REFERENCES `STORE_TEST`.`USUARIO` (`IDUSUARIO`))
ENGINE = InnoDB;

INSERT INTO `STORE_TEST`.`USUARIO` (NOMBRE, APELLIDO, EDAD, CORREO, PASSWORD) value ("admin", "admin", 10, "admin@gmail.com", "admin123");