import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { OrderSummary } from "@point_of_sale/app/screens/product_screen/order_summary/order_summary";
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";
import { SelectionPopup } from "@point_of_sale/app/components/popups/selection_popup/selection_popup";
import { sprintf } from "@web/core/utils/strings";

patch(ControlButtons.prototype, {
    async clickCustomDiscount() {
        const order = this.pos.getOrder();
        let selected_orderline = order.getSelectedOrderline();
        if (selected_orderline) {
            selected_orderline.setDiscount(5);
        }
    },
    async clickLastOrderButton() {
        const order = this.pos.getOrder();
        const partner = order.getPartner();
        if (partner) {
            let domain = [['partner_id', '=', partner.id]];
            const orders = await this.pos.data.searchRead("pos.order", domain, ["name","amount_total"], {
                limit: 5,
            });
            if (orders.length > 0) {
                var order_list = orders.map((o) => {
                    return { 'label': sprintf("%s -TOTAL: %s", o.name, o.amount_total) };
                });
                await this.dialog.add(SelectionPopup, {
                    title: 'Last 5 orders',
                    list: order_list,
                    getPayload: (olist) => {},
                });
            } else {
                await this.dialog.add(AlertDialog, {
                    body: "No previous orders found"
                });
            }
        } else {
            await this.dialog.add(AlertDialog, {
                body: "No previous orders found"
            });
        }
    }
});

patch(OrderSummary.prototype, {
    _setValue(val) {
        super._setValue(val);
        const selectedLine = this.currentOrder.getSelectedOrderline();
        if (selectedLine && selectedLine.product_id.standard_price) {
            let price_unit = selectedLine.getUnitPrice() * (1.0 - (selectedLine.getDiscount() / 100.0));
            if (selectedLine.product_id.standard_price > price_unit) {
                this.dialog.add(AlertDialog,  {
                    title: 'Warning', 
                    body: 'Product price set below cost of product.' 
                });
            }
        }
    }
});

patch(PosOrder.prototype, {
    saved_amount(){
        let saved_amount = this.lines.reduce((rem, line) => {
            let diffrence = (line.product_id.list_price * line.qty) - line.getBasePrice();
            return rem + diffrence;
        }, 0);
        if (savedAmount > 0) {
            return saved_amount;
        }
        return 0;
    }
});
