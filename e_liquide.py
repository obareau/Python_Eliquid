import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime
import matplotlib.pyplot as plt
from math import ceil
from fpdf import FPDF
import csv

class EliquidCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur de E-Liquide")

        # Variables générales
        self.recipe_name = tk.StringVar(value="Ma Recette")
        self.arome_proportion = tk.DoubleVar(value=10)
        self.total_volume = tk.DoubleVar(value=100)
        self.nicotine_target = tk.DoubleVar(value=3)
        self.booster_nicotine = tk.DoubleVar(value=20)
        self.base_pg = tk.DoubleVar(value=50)
        self.base_vg = tk.DoubleVar(value=50)
        self.booster_pg = tk.DoubleVar(value=50)
        self.booster_vg = tk.DoubleVar(value=50)
        self.arome_pg = tk.DoubleVar(value=100)
        self.arome_vg = tk.DoubleVar(value=0)
        self.base_nicotined = tk.BooleanVar(value=False)
        self.base_nicotine = tk.DoubleVar(value=0)
        self.base_nicotine_volume = tk.DoubleVar(value=0)
        self.final_nicotine = tk.DoubleVar(value=0)
        self.num_boosters = tk.IntVar(value=0)
        self.creation_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Initialisation correcte

        # Interface utilisateur
        self.create_widgets()

    def create_widgets(self):
        # Nom de la recette
        ttk.Label(self.root, text="Nom de la Recette :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.recipe_name, width=30).grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        # Date de création de la recette
        ttk.Label(self.root, text=f"Date de Création : {self.creation_date}").grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="w")
        # Section Volume Total
        ttk.Label(self.root, text="Volume Total (ml) :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.total_volume, width=10).grid(row=1, column=1, padx=5, pady=5)

        # Section Arôme
        ttk.Label(self.root, text="Proportion d'arôme (%) :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.arome_proportion, width=10).grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Taux PG/VG de l'arôme (%) :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.arome_pg, width=5).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.arome_vg, width=5).grid(row=3, column=2, padx=5, pady=5, sticky="w")

        # Section Nicotine
        ttk.Label(self.root, text="Taux de Nicotine voulu (mg/ml) :").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.nicotine_target, width=10).grid(row=4, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Taux PG/VG de la base (%) :").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.base_pg, width=5).grid(row=5, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.base_vg, width=5).grid(row=5, column=2, padx=5, pady=5, sticky="w")
        ttk.Label(self.root, text="Taux PG/VG du booster (%) :").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.booster_pg, width=5).grid(row=6, column=1, padx=5, pady=5, sticky="w")
        ttk.Entry(self.root, textvariable=self.booster_vg, width=5).grid(row=6, column=2, padx=5, pady=5, sticky="w")

        # Base Nicotinée
        ttk.Checkbutton(self.root, text="Base déjà nicotinée", variable=self.base_nicotined, command=self.toggle_base_nicotine).grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")
        ttk.Label(self.root, text="Taux de Nicotine de la base (mg/ml) :").grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.base_nicotine_entry = ttk.Entry(self.root, textvariable=self.base_nicotine, width=10, state="disabled")
        self.base_nicotine_entry.grid(row=8, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Volume Base Nicotinée (ml) :").grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.base_nicotine_volume_entry = ttk.Entry(self.root, textvariable=self.base_nicotine_volume, width=10, state="disabled")
        self.base_nicotine_volume_entry.grid(row=9, column=1, padx=5, pady=5)

        # Boutons principaux
        ttk.Button(self.root, text="Calculer", command=self.calculate).grid(row=10, column=0, columnspan=2, padx=10, pady=10)
        ttk.Button(self.root, text="Sauvegarder Recette", command=self.save_recipe).grid(row=11, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(self.root, text="Charger Recette", command=self.load_recipe).grid(row=12, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(self.root, text="Exporter en PDF", command=self.export_pdf).grid(row=13, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(self.root, text="Exporter en CSV", command=self.export_csv).grid(row=15, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(self.root, text="Afficher les Statistiques", command=self.show_pie_chart).grid(row=16, column=0, columnspan=2, padx=10, pady=5)

        # Résultats
        self.results_text = tk.Text(self.root, width=50, height=10, state="disabled")
        self.results_text.grid(row=14, column=0, columnspan=3, padx=10, pady=10)

    def toggle_base_nicotine(self):
        if self.base_nicotined.get():
            self.base_nicotine_entry.config(state="normal")
            self.base_nicotine_volume_entry.config(state="normal")
        else:
            self.base_nicotine_entry.config(state="disabled")
            self.base_nicotine_volume_entry.config(state="disabled")
            self.base_nicotine.set(0)
            self.base_nicotine_volume.set(0)

    def calculate(self):
        total_volume = self.total_volume.get()
        arome_proportion = self.arome_proportion.get()
        nicotine_target = self.nicotine_target.get()
        booster_nicotine = self.booster_nicotine.get()
        base_nicotine = self.base_nicotine.get()
        base_nicotine_volume = self.base_nicotine_volume.get()

        volume_arome = (arome_proportion / 100) * total_volume
        if self.base_nicotined.get() and base_nicotine_volume > 0:
            volume_booster = 0
            volume_base = total_volume - volume_arome - base_nicotine_volume
            self.final_nicotine.set((base_nicotine * base_nicotine_volume) / total_volume)
        else:
            volume_booster = (nicotine_target * total_volume) / booster_nicotine
            volume_base = total_volume - volume_arome - volume_booster
            self.final_nicotine.set(nicotine_target)

        num_boosters = ceil(volume_booster / 10)
        self.num_boosters.set(num_boosters)

        if volume_base < 0:
            messagebox.showerror("Erreur", "Le taux de nicotine ou d'arôme est trop élevé pour le volume total.")
            return

        results = (
            f"Nom de la Recette : {self.recipe_name.get()}\n"
            f"Volume Total : {total_volume:.2f} ml\n"
            f"Volume Arôme : {volume_arome:.2f} ml\n"
            f"Volume Booster : {volume_booster:.2f} ml ({num_boosters} boosters de 10 ml)\n"
            f"Volume Base : {volume_base:.2f} ml\n"
            f"Base Nicotinée Utilisée : {base_nicotine_volume:.2f} ml à {base_nicotine} mg/ml\n"
            f"Taux Final de Nicotine : {self.final_nicotine.get():.2f} mg/ml"
        )
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, results)
        self.results_text.config(state="disabled")

    def save_recipe(self):
        recipe = {
            "nom": self.recipe_name.get(),
            "volume_total": self.total_volume.get(),
            "arome_proportion": self.arome_proportion.get(),
            "nicotine_target": self.nicotine_target.get(),
            "final_nicotine": self.final_nicotine.get(),
            "num_boosters": self.num_boosters.get(),
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(recipe, f, indent=4)
            messagebox.showinfo("Succès", f"Recette sauvegardée dans {file_path}")

    def load_recipe(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not file_path:
            return
        try:
            with open(file_path, "r") as f:
                recipe = json.load(f)
            self.recipe_name.set(recipe.get("nom", "Ma Recette"))
            self.total_volume.set(recipe.get("volume_total", 100))
            self.arome_proportion.set(recipe.get("arome_proportion", 10))
            self.nicotine_target.set(recipe.get("nicotine_target", 3))
            self.final_nicotine.set(recipe.get("final_nicotine", 0))
            self.num_boosters.set(recipe.get("num_boosters", 0))
            messagebox.showinfo("Succès", f"Recette chargée depuis {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement de la recette : {e}")

    def export_pdf(self):
        """Exporte la recette actuelle en PDF."""
        recipe = {
            "Nom de la recette": self.recipe_name.get(),
            "Date de création": self.creation_date,  # Ajout de la date de création
            "Volume total (ml)": self.total_volume.get(),
            "Proportion d'arôme (%)": self.arome_proportion.get(),
            "Taux PG/VG de l'arôme": f"{self.arome_pg.get()}% / {self.arome_vg.get()}%",
            "Taux de nicotine voulu (mg/ml)": self.nicotine_target.get(),
            "Taux PG/VG de la base": f"{self.base_pg.get()}% / {self.base_vg.get()}%",
            "Taux PG/VG des boosters": f"{self.booster_pg.get()}% / {self.booster_vg.get()}%",
            "Volume d'arôme (ml)": (self.arome_proportion.get() / 100) * self.total_volume.get(),
            "Nombre de boosters nécessaires": self.num_boosters.get(),
            "Volume total de boosters (ml)": self.num_boosters.get() * 10,
            "Taux final de nicotine (mg/ml)": self.final_nicotine.get(),
            "Base nicotinée utilisée": f"{self.base_nicotine_volume.get()} ml à {self.base_nicotine.get()} mg/ml" \
            if self.base_nicotined.get() else "Non utilisée",
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=self.recipe_name.get(), filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Titre du PDF
            pdf.cell(200, 10, txt=f"Recette de E-Liquide : {self.recipe_name.get()}", ln=True, align="C")
            pdf.ln(10)  # Saut de ligne

            # Contenu de la recette
            for key, value in recipe.items():
                pdf.cell(200, 10, txt=f"{key} : {value}", ln=True)

            pdf.output(file_path)
            messagebox.showinfo("Succès", f"Recette exportée en PDF avec succès sous {file_path} !")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export en PDF : {e}")

    def export_csv(self):
        """Exporte la recette actuelle en CSV."""
        recipe = {
            "Nom de la recette": self.recipe_name.get(),
            "Volume total (ml)": self.total_volume.get(),
            "Proportion d'arôme (%)": self.arome_proportion.get(),
            "Taux PG/VG de l'arôme": f"{self.arome_pg.get()}% / {self.arome_vg.get()}%",
            "Taux de nicotine voulu (mg/ml)": self.nicotine_target.get(),
            "Taux PG/VG de la base": f"{self.base_pg.get()}% / {self.base_vg.get()}%",
            "Taux PG/VG des boosters": f"{self.booster_pg.get()}% / {self.booster_vg.get()}%",
            "Volume d'arôme (ml)": (self.arome_proportion.get() / 100) * self.total_volume.get(),
            "Nombre de boosters nécessaires": self.num_boosters.get(),
            "Volume total de boosters (ml)": self.num_boosters.get() * 10,
            "Taux final de nicotine (mg/ml)": self.final_nicotine.get(),
            "Base nicotinée utilisée": f"{self.base_nicotine_volume.get()} ml à {self.base_nicotine.get()} mg/ml" \
            if self.base_nicotined.get() else "Non utilisée",
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=self.recipe_name.get(), filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Clé", "Valeur"])  # En-têtes du CSV
                for key, value in recipe.items():
                    writer.writerow([key, value])  # Écriture des données

            messagebox.showinfo("Succès", f"Recette exportée en CSV avec succès sous {file_path} !")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export en CSV : {e}")

    def show_pie_chart(self):
        # Récupérer les volumes
        
        total_volume = self.total_volume.get()
        arome_proportion = self.arome_proportion.get()
        nicotine_target = self.nicotine_target.get()
        booster_nicotine = self.booster_nicotine.get()
        base_nicotine = self.base_nicotine.get() # Ne pas supprimer cette ligne mmême si variable pas utilisée
        base_nicotine_volume = self.base_nicotine_volume.get()

        volume_arome = (arome_proportion / 100) * total_volume
        if self.base_nicotined.get() and base_nicotine_volume > 0:
            volume_booster = 0
            volume_base = total_volume - volume_arome - base_nicotine_volume
        else:
            volume_booster = (nicotine_target * total_volume) / booster_nicotine
            volume_base = total_volume - volume_arome - volume_booster

        # Créer les labels et valeurs pour le graphique
        labels = ['Arôme', 'Booster', 'Base Nicotinée', 'Base']
        values = [volume_arome, volume_booster, base_nicotine_volume, volume_base]

        # Créer le camembert
        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        # Ajouter le nom de la recette et la date de création au titre
        plt.title(f"Proportions de la Recette de E-liquide : {self.recipe_name.get()}\nDate de création : {self.creation_date}")
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = EliquidCalculator(root)
    root.mainloop()

