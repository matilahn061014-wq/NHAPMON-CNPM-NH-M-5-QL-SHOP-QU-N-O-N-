// ====== KHO HÀNG (Inventory) ======
let inventory = {};

// ====== HÀM TẠO PHIẾU NHẬP ======
function createImportReceipt(date, supplier) {
  return {
    date,
    supplier,
    items: []
  };
}

// ====== THÊM CHI TIẾT SẢN PHẨM ======
function addItemToReceipt(receipt, productName, color, size, quantity, costPrice) {
  receipt.items.push({
    productName,
    color,
    size,
    quantity,
    costPrice
  });
}

// ====== CẬP NHẬT TỒN KHO ======
function updateInventory(receipt) {
  receipt.items.forEach(item => {
    const key = `${item.productName}-${item.color}-${item.size}`;

    if (!inventory[key]) {
      inventory[key] = {
        productName: item.productName,
        color: item.color,
        size: item.size,
        quantity: 0,
        costPrice: item.costPrice
      };
    }

    inventory[key].quantity += item.quantity;
  });
}

// ====== HOÀN TẤT PHIẾU NHẬP ======
function completeReceipt(receipt) {
  updateInventory(receipt);
  console.log("✅ Phiếu nhập hàng đã hoàn tất!");
}

// ====== CHẠY THỬ ======

// 1. Tạo phiếu nhập
let receipt = createImportReceipt("2025-12-30", "Công ty ABC");

// 2. Thêm sản phẩm
addItemToReceipt(receipt, "Áo thun", "Đen", "M", 50, 120000);
addItemToReceipt(receipt, "Áo thun", "Đen", "L", 30, 125000);
addItemToReceipt(receipt, "Quần jean", "Xanh", "32", 20, 250000);

// 3. Hoàn tất phiếu (tự động cộng tồn kho)
completeReceipt(receipt);

// 4. Kiểm tra tồn kho
console.log("📦 TỒN KHO HIỆN TẠI:");
console.table(inventory);
