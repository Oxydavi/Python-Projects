import GPUtil as gp
import tkinter as tk


def gpu_info():
    gpus = gp.getGPUs()
    gpus_list = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temp = f"{gpu.temperature}°С"

        gpus_list.append((
            gpu_id,
            gpu_name,
            gpu_load,
            gpu_free_memory,
            gpu_used_memory,
            gpu_total_memory,
            gpu_temp
        ))

    return gpus_list


def update_info():
    gpu_info_list = gpu_info()
    text.delete("1.0", tk.END)
    for gpu in gpu_info_list:
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temp = gpu
        info = f"GPU ID: {gpu_id}\n" \
               f"GPU Name: {gpu_name}\n" \
               f"GPU Load: {gpu_load}\n" \
               f"GPU Free Memory: {gpu_free_memory}\n" \
               f"GPU Used Memory: {gpu_used_memory}\n" \
               f"GPU Total Memory: {gpu_total_memory}\n" \
               f"GPU Temperature: {gpu_temp}\n\n"
        text.insert(tk.END, info)

    root.after(1000, update_info)

root = tk.Tk()
root.title("GPU Information")

text = tk.Text(root, height=7, width=45)
text.pack()
root.resizable(False, False)
update_info()

root.mainloop()