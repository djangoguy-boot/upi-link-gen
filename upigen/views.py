from django.shortcuts import render
import qrcode
import io
import base64

def home(request):
    context = {}
    if request.method == "POST":
        upi_id = request.POST.get("upi_id")
        name = request.POST.get("name")
        amount = request.POST.get("amount")

        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}"
        context["upi_link"] = upi_link

        # Generate QR code
        qr = qrcode.make(upi_link)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        qr_b64 = base64.b64encode(buffer.getvalue()).decode()
        context["qr_code"] = qr_b64

    return render(request, "index.html", context)
