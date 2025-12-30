// ====== DỮ LIỆU TỒN KHO ======
let inventory = {};
let inventoryHistory = [];

// ====== HÀM TẠO KEY ======
function createKey(product, color, size) {
  return `${product}-${color}-${size}`;
}

// ====== NHẬP KHO ======
function importStock(product, color, size, quantity) {
  const key = createKey(product, color, size);

  if (!inventory[key]) {
    inventory[key] = { product, color, size, quantity: 0 };
  }

  inventory[key].quantity += quantity;

  inventoryHistory.push({
    type: "IMPORT",
    product,
    color,
    size,
    quantity,
    date: new Date()
  });
}

// ====== XUẤT KHO ======
function exportStock(product, color, size, quantity) {
  const key = createKey(product, color, size);

  if (!inventory[key] || inventory[key].quantity < quantity) {
    console.log("❌ Không đủ tồn kho");
    return;
  }

  inventory[key].quantity -= quantity;

  inventoryHistory.push({
    type: "EXPORT",
    product,
    color,
    size,
    quantity,
    date: new Date()
  });
}

// ====== XEM TỔNG QUAN TỒN KHO ======
function viewInventoryOverview() {
  console.log("📦 TỔNG QUAN TỒN KHO");
  console.table(inventory);
}

// ====== LỌC TỒN KHO THEO PHIÊN BẢN ======
function filterInventory(product, color, size) {
  const key = createKey(product, color, size);
  console.log("🔍 CHI TIẾT TỒN KHO:");
  console.table(inventory[key] ? [inventory[key]] : []);
}

// ====== XEM LỊCH SỬ NHẬP / XUẤT ======
function viewRecentHistory(limit = 5) {
  console.log("📜 LỊCH SỬ NHẬP / XUẤT GẦN NHẤT");
  console.table(inventoryHistory.slice(-limit));
}

// ====== ĐIỀU CHỈNH TỒN KHO THỦ CÔNG ======
function adjustInventory(product, color, size, newQuantity, reason) {
  const key = createKey(product, color, size);

  if (!inventory[key]) {
    inventory[key] = { product, color, size, quantity: 0 };
  }

  const oldQuantity = inventory[key].quantity;
  inventory[key].quantity = newQuantity;

  inventoryHistory.push({
    type: "ADJUST",
    product,
    color,
    size,
    oldQuantity,
    newQuantity,
    reason,
    date: new Date()
  });
}

// ====== CHẠY THỬ ======

// Nhập kho
importStock("Áo thun", "Đen", "M", 100);
importStock("Áo thun", "Đen", "L", 50);
importStock("Quần jean", "Xanh", "32", 40);

// Xuất kho
exportStock("Áo thun", "Đen", "M", 20);

// Điều chỉnh tồn kho
adjustInventory("Áo thun", "Đen", "L", 60, "Kiểm kê cuối ngày");

// Xem tồn kho
viewInventoryOverview();

// Lọc theo phiên bản
filterInventory("Áo thun", "Đen", "M");

// Xem lịch sử
viewRecentHistory();