# Retail + Manufacturing + Logistics Data Model

## Tables Overview

* Product & Inventory → `Products`, `Warehouses`, `InventoryLevels`
* Sales → `Order_Summary`, `Order_Details`
* Manufacturing → `ProductionRuns`, `Machines`, `Employees`
* Logistics → `Shipments`
* GPS → `Routes`
* Dimensions → `Stores`, `Customers`

---

## Sales Module

### `Order_Summary`

| Field         | Type      | Description                  |
| ------------- | --------- | ---------------------------- |
| OrderID       | TEXT (PK) | Unique order identifier      |
| OrderDate     | DATE      | Date of order placement      |
| StoreID       | TEXT (FK) | Store where order was placed |
| CustomerID    | TEXT (FK) | Linked customer              |
| EmployeeID    | TEXT (FK) | Employee handling the order  |
| TotalAmount   | DECIMAL   | Total after tax + shipping   |
| PaymentMethod | TEXT      | Cash, Card, UPI              |
| Status        | TEXT      | Pending, Delivered, etc.     |
| Channel       | TEXT      | Online, In-Store, Mobile App |
| Currency      | TEXT      | INR only                     |
| DeliveryType  | TEXT      | Express, Same Day, Standard  |
| TaxAmount     | DECIMAL   | GST applied                  |
| ShippingFee   | DECIMAL   | Shipping charge              |

### `Order_Details`

| Field        | Type      | Description                 |
| ------------ | --------- | --------------------------- |
| DetailID     | TEXT (PK) | Unique line item identifier |
| OrderID      | TEXT (FK) | References `Order_Summary`  |
| SKU          | TEXT (FK) | Product SKU                 |
| Qty          | INT       | Quantity sold               |
| UnitPrice    | DECIMAL   | Price per unit              |
| Discount     | DECIMAL   | Discount per unit           |
| Returned     | BOOLEAN   | Return flag                 |
| ReturnReason | TEXT      | Reason if returned          |
| UnitCost     | DECIMAL   | Company cost per unit       |

---

## Product & Inventory Module

### `Products`

| Field         | Type      | Description                       |
| ------------- | --------- | --------------------------------- |
| SKU           | TEXT (PK) | Unique product ID                 |
| Name          | TEXT      | Product name                      |
| Category      | TEXT      | Category (Electronics, etc.)      |
| Subcategory   | TEXT      | Specific type (Smartphones, etc.) |
| Brand         | TEXT      | Brand name                        |
| CostPrice     | DECIMAL   | Cost to company                   |
| SellPrice     | DECIMAL   | Retail price                      |
| Status        | TEXT      | Active, OOS, Discontinued         |
| LaunchDate    | DATE      | Launch date                       |
| AverageRating | DECIMAL   | Rating (0–5)                      |

### `Warehouses`

| Field       | Type      | Description         |
| ----------- | --------- | ------------------- |
| WarehouseID | TEXT (PK) | Unique warehouse ID |
| Name        | TEXT      | Warehouse name      |
| Location    | TEXT      | City/region         |
| Capacity    | INT       | Max capacity        |
| StorageType | TEXT      | Cold, Dry, General  |

### `InventoryLevels`

| Field         | Type      | Description             |
| ------------- | --------- | ----------------------- |
| SKU           | TEXT (FK) | References `Products`   |
| WarehouseID   | TEXT (FK) | References `Warehouses` |
| Date          | DATE      | Snapshot date           |
| OnHandQty     | INT       | In stock                |
| ReservedQty   | INT       | Reserved stock          |
| ReorderPoint  | INT       | Trigger point           |
| SafetyStock   | INT       | Minimum required        |
| DaysToRestock | INT       | Days to refill          |
| ShelfLifeDays | INT       | Days until expiry       |

---

## Manufacturing Module

### `ProductionRuns`

| Field          | Type      | Description         |
| -------------- | --------- | ------------------- |
| ProdRunID      | TEXT (PK) | Run identifier      |
| Date           | DATE      | Run date            |
| MachineID      | TEXT (FK) | Machine used        |
| SKU            | TEXT (FK) | Product             |
| PlannedUnits   | INT       | Planned qty         |
| ActualUnits    | INT       | Actual qty          |
| ScrapUnits     | INT       | Rejected qty        |
| DowntimeMins   | INT       | Downtime duration   |
| DowntimeReason | TEXT      | Reason for downtime |
| EmployeeID     | TEXT (FK) | Responsible worker  |

### `Machines`

| Field        | Type      | Description          |
| ------------ | --------- | -------------------- |
| MachineID    | TEXT (PK) | Unique machine ID    |
| MachineType  | TEXT      | Equipment type       |
| PurchaseDate | DATE      | Date of purchase     |
| MachineBrand | TEXT      | Brand                |
| Location     | TEXT      | Site/warehouse       |
| Status       | TEXT      | Active, Repair, etc. |
| EmployeeID   | TEXT (FK) | Assigned operator    |

### `Employees`

| Field            | Type      | Description                        |
| ---------------- | --------- | ---------------------------------- |
| EmployeeID       | TEXT (PK) | Unique ID                          |
| Name             | TEXT      | Employee name                      |
| Role             | TEXT      | Operator, Driver, etc.             |
| Department       | TEXT      | Dept. (Logistics, Sales, etc.)     |
| HireDate         | DATE      | Hiring date                        |
| Salary           | DECIMAL   | Monthly salary                     |
| Status           | TEXT      | Active, On Leave, Terminated       |
| Location         | TEXT      | City                               |
| Shift            | TEXT      | Morning, Night, etc.               |
| PerformanceScore | DECIMAL   | 0–5                                |
| VehicleType      | TEXT      | If driver                          |
| LicenseNumber    | TEXT      | If driver                          |
| Availability     | TEXT      | If driver (Available, Trip, Break) |
| MachineID        | TEXT (FK) | Linked machine if operator         |
| ShipmentID       | TEXT      | Linked shipment if driver          |
| Phone            | TEXT      | Contact number                     |
| Email            | TEXT      | Contact email                      |
| DateOfBirth      | DATE      | DOB                                |
| Gender           | TEXT      | M/F/Other                          |
| AttendanceRate   | DECIMAL   | Attendance %                       |

---

## Logistics Module

### `Shipments`

| Field        | Type      | Description                |
| ------------ | --------- | -------------------------- |
| ShipmentID   | TEXT (PK) | Unique ID                  |
| OrderID      | TEXT (FK) | References `Order_Summary` |
| WarehouseID  | TEXT (FK) | Source warehouse           |
| ShipDate     | DATE      | Dispatch date              |
| DeliveryDate | DATE      | Delivery date              |
| DistanceKM   | DECIMAL   | Distance covered           |
| Status       | TEXT      | Delivered, Returned, etc.  |
| DelayReason  | TEXT      | Traffic, Weather, etc.     |
| ShippingCost | DECIMAL   | Cost of shipping           |
| EmployeeID   | TEXT (FK) | Responsible driver         |

---

## GPS / Routes Module

### `Routes`

| Field            | Type      | Description          |
| ---------------- | --------- | -------------------- |
| RouteID          | TEXT (PK) | Unique ID            |
| ShipmentID       | TEXT (FK) | Linked shipment      |
| StartLocation    | TEXT      | From address         |
| EndLocation      | TEXT      | Destination address  |
| EstimatedTimeMin | INT       | Expected travel time |
| ActualTimeMin    | INT       | Actual travel time   |
| TrafficLevel     | TEXT      | Low, Medium, High    |
| WeatherCondition | TEXT      | Clear, Rain, etc.    |
| EmployeeID       | TEXT (FK) | Driver               |
| RouteCost        | DECIMAL   | Cost of route        |
| StartTime        | DATETIME  | Departure            |
| EndTime          | DATETIME  | Arrival              |

---

## Dimensions

### `Stores`

| Field             | Type      | Description                |
| ----------------- | --------- | -------------------------- |
| StoreID           | TEXT (PK) | Store identifier           |
| Name              | TEXT      | Store name                 |
| Region            | TEXT      | Region (e.g., North India) |
| StoreType         | TEXT      | Flagship, Outlet, Online   |
| ManagerID         | TEXT (FK) | Store manager              |
| IsActive          | BOOLEAN   | Active flag                |
| InventoryCapacity | INT       | Max units                  |

### `Customers`

| Field           | Type      | Description            |
| --------------- | --------- | ---------------------- |
| CustomerID      | TEXT (PK) | Customer ID            |
| Name            | TEXT      | Customer name          |
| Email           | TEXT      | Email address          |
| Phone           | TEXT      | Phone number           |
| Location        | TEXT      | City                   |
| SignupDate      | DATE      | Signup date            |
| CustomerSegment | TEXT      | Regular, VIP, One-time |

---

## Status Reference

### Orders / Order\_Details

* Pending → Order created, not processed
* Processing → Picking/packing ongoing
* Shipped → Left warehouse
* Delivered → Successfully fulfilled
* Cancelled → Stopped before/during processing
* Exchanged → Returned & replaced
* Refunded → Returned & refunded

### Shipments

* Pending → Created, not dispatched
* Out for Delivery → With driver, last mile
* In Transit → Moving, not yet delivered
* Delivered → Successful delivery
* Returned → Sent back by customer
* Failed → Delivery attempt unsuccessful
