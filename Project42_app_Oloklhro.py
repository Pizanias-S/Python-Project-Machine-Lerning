# ΠΛΗΠΛΡΟ 2021 - 2022
# Project 42 - Στέφανος Πιζάνιας


# Εισαγωγή Βιβλιοθηκών
import pandas as pd
import matplotlib.pyplot as plt
from statistics import median_low, median_high
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def main():

    # Κατασκευή παραθύρου με το tkinter
    root = Tk()
    root.geometry("410x850+650+0")
    root.resizable(False, False)
    root.title("Project 42")

    # Σταθερές μεγέθους πίνακα δεδομένων
    ROWS = 1484
    COLS = 10


    onomata = ["CYT", "NUC", "MIT", "ME3", "ME2", "ME1", "EXC", "VAC", "POX", "ERL"]

    onomata2 = ["mcg", "gvh", "alm", "mit", "erl", "pox", "vac", "nuc"]

    # Συνάρτηση υπολογισμού του αριθμητικού μέσου(μέσο όρο)
    def arithmitikosmesos(classdisdataframe, nms):

        arithmitikosMesos = classdisdataframe[nms].mean()
        print("Ο Αριθμητικός Μέσος είναι:")
        print(arithmitikosMesos)

    # Συνάρτηση υπολογισμού της μέσης τιμής(διάμεσος)
    def meshtimh(classdisdataframe, nms):

        meshTimh = classdisdataframe[nms].median()
        print("Η Μέση Τιμή είναι:")
        print(meshTimh)

    # Συνάρτηση υπολογισμού της χαμηλής μέσης τιμής
    def lowmeshtimh(classdisdataframe, nms):

        med = lambda x: median_low(x)
        lowMeshTimh = classdisdataframe[nms].apply(med)
        print("Η Χαμηλή Μέση Τιμή είναι:")
        print(lowMeshTimh.astype(float))

    # Συνάρτηση υπολογισμού της υψηλής μέσης τιμής
    def highmeshtimh(classdisdataframe, nms):

        med = lambda y: median_high(y)
        highMeshTimh = classdisdataframe[nms].apply(med)
        print("Η Υψηλή Μέση Τιμή είναι:")
        print(highMeshTimh.astype(float))

    # Συνάρτηση υπολογισμού της τυπικής απόκλισης
    def tupikhapoklish(classdisdataframe, nms):

        tupikhApoklish = classdisdataframe[nms].std()
        print("Η Τυπική Απόκλιση του Δείγματος είναι:")
        print(tupikhApoklish)
        return tupikhApoklish

    # Συνάρτηση υπολογισμού της διακύμανσης
    def funcdiakimansh(classdisdataframe, nms):

        diakimansh = classdisdataframe[nms].var()
        print("Η Διακύμανση του Δείγματος είναι:")
        print(diakimansh)
        return diakimansh

    # Συνάρτηση σχεδιασμού του ραβδογράμματος για την τυπική απόκλιση
    def sxediasmostupikhapoklish(tupikiapolkisi):

        # plt.close("all")
        tupikiapolkisi.plot.bar()
        plt.show()

    # Συνάρτηση σχεδιασμού του ραβδογράμματος για τη διακύμανση
    def sxediasmosdiakimansh(sxdiakimansh):

        # plt.close("all")
        sxdiakimansh.plot.bar()
        plt.show()

    # Συνάρτηση για τις πληροφορίες της inertia
    def inertia_info():
        messagebox.showinfo(title="Inertia Info",
                            message="Θα εμφανιστούν τα αποτελέσματα για την inertia που έχει ο κάθε αριθμός cluster και"
                                    " μια γραφική παράσταση της inertia/cluster")

    # Συνάρτηση για τις πληροφορίες για τις υποεργασίες 1,2,3
    def upo_info():
        messagebox.showinfo(title="Υποεργασίες 1,2,3",
                            message="Θα εμφανιστούν τα αποτελέσματα για τις υποεργασίες 1-3 που δεν"
                                    " επηρεάζουν τα βασικά ερωτήματα της εργασίας.")

    # Συνάρτηση για τις πληροφορίες των Cluster
    def cluster_info():
        messagebox.showinfo(title="Cluster Info", message="Επιλέξτε απο 2-8 ομαδοποιήσεις να γίνουν και απο 2-8 "
                                                          "χαρακτηριστικά για την ομαδοποίηση. Θα εμφανιστεί η "
                                                          "γραφική παράσταση για τις επιλεγμένες ομαδοποιήσεις. ")

    # Συνάρτηση για την επιλογή τεστ
    def upo_exe():

        # Μετατρέπει το yeastData σε τύπο list
        classDistributionList = yeastData["ClassDis"].to_list()

        # Δίνουμε δυαδικές τιμές στο classDistributionList
        for t in range(len(classDistributionList)):

            if classDistributionList[t] == "CYT":
                classDistributionList[t] = "1000000000"
            elif classDistributionList[t] == "NUC":
                classDistributionList[t] = "0100000000"
            elif classDistributionList[t] == "MIT":
                classDistributionList[t] = "0010000000"
            elif classDistributionList[t] == "ME3":
                classDistributionList[t] = "0001000000"
            elif classDistributionList[t] == "ME2":
                classDistributionList[t] = "0000100000"
            elif classDistributionList[t] == "ME1":
                classDistributionList[t] = "0000010000"
            elif classDistributionList[t] == "EXC":
                classDistributionList[t] = "0000001000"
            elif classDistributionList[t] == "VAC":
                classDistributionList[t] = "0000000100"
            elif classDistributionList[t] == "POX":
                classDistributionList[t] = "0000000010"
            elif classDistributionList[t] == "ERL":
                classDistributionList[t] = "0000000001"

        rows, cols = (ROWS, COLS)
        y = []

        # Σπάμε την λίστα classDistributionList σε λίστες ανα ψηφίο
        for k in range(len(classDistributionList)):
            z = []

            for j in range(cols):
                z.append(int(classDistributionList[k][j]))

            y.append(z)

        # Μετατρέπουμε την ολοκληρωμένη δυαδική λίστα σε τύπο dataframe για να την επεξεργαστούμε ευκολότερα
        classDisDataFrame = pd.DataFrame(y,
                                         columns=["CYT", "NUC", "MIT", "ME3", "ME2", "ME1", "EXC", "VAC", "POX", "ERL"])

        print(classDisDataFrame)

        # Αριθμητικός Μέσος
        arithmitikosmesos(classDisDataFrame, onomata)

        # Μέση Τιμή
        meshtimh(classDisDataFrame, onomata)

        # Χαμηλή Μέση Τιμή
        lowmeshtimh(classDisDataFrame, onomata)

        # Υψηλή Μέση Τιμή
        highmeshtimh(classDisDataFrame, onomata)

        # Τυπική Απόκλιση
        tupap = tupikhapoklish(classDisDataFrame, onomata)

        # Διακύμανση
        dia = funcdiakimansh(classDisDataFrame, onomata)

        # Σχεδιασμός Τυπικής Απόκλισης
        sxediasmostupikhapoklish(tupap)

        # Σχεδιασμός Διακύμανσης
        sxediasmosdiakimansh(dia)

    # Συνάρτηση για τον υπολογισμό της Inertia
    def inertia_exe():

        yeast_data = yeastData.loc[:, onomata2]

        pca = PCA(2)

        dff = pca.fit_transform(yeast_data)
        # Για να βρούμε τον βέλτιστο αριθμό clusters τρέχουμε τον αλγόριθμο για όλα τα δυνατά clusters
        no_of_clusters = range(2, 9)
        inertia = []

        for f in no_of_clusters:
            kmeans = KMeans(n_clusters=f)
            kmeans.fit_predict(dff)

            u = kmeans.inertia_
            inertia.append(u)
            print(f"Η inertia για: {f} Clusters είναι: {u}")

        # Φτιάχνουμε μια γραφική παράσταση ώστε να βρούμε το βέλτιστο αριθμό clusters με την elbow method
        fig, (ax1) = plt.subplots(1, figsize=(16, 6))
        xx = np.arange(len(no_of_clusters))
        ax1.plot(xx, inertia)
        ax1.set_xticks(xx)
        ax1.set_xticklabels(no_of_clusters, rotation="vertical")
        plt.xlabel("Αριθμός των clusters")
        plt.ylabel("Αριθμός Inertia")
        plt.title("Γραφική παράσταση Inertia για όλα τα cluster")
        plt.show()

    # Συνάρτηση για τον υπολογισμό και την εμφάνιση των clusters ανάλογα με πόσα έχει επιλέξει ο χρήστης
    def cluster_exe():

        # Τρέχουμε τον Kmeans βάζοντας από το yeastData μόνο τις μεταβλητές mcg, gvh, alm, mit, erl, pox, vac, nuc
        yeast_data = yeastData.loc[:, onomata2]

        # Ελέγχουμε ποιες μεταβλητές επέλεξε ο χρήστης
        a = 0
        if chVar12.get() == 0:
            del yeast_data["mcg"]
            a = a + 1
        if chVar13.get() == 0:
            del yeast_data["gvh"]
            a = a + 1
        if chVar14.get() == 0:
            del yeast_data["alm"]
            a = a + 1
        if chVar15.get() == 0:
            del yeast_data["mit"]
            a = a + 1
        if chVar16.get() == 0:
            del yeast_data["erl"]
            a = a + 1
        if chVar17.get() == 0:
            del yeast_data["pox"]
            a = a + 1
        if chVar18.get() == 0:
            del yeast_data["vac"]
            a = a + 1
        if chVar19.get() == 0:
            del yeast_data["nuc"]
            a = a + 1

        # Error αν ο χρήστης δεν επιλέξει τουλάχιστον 2 μεταβλητές
        if a >= 7:
            messagebox.showerror(title="Cluster Error", message="Πρέπει να επιλέξετε τουλάχιστον 2 στοιχεία")
            return 0
        print(yeast_data)
        # Επιλογή του χρήστη για τον αριθμό των clusters
        numberOfClusters = clusters.get()
        pca = PCA(2)

        # Μετατρέπουμε τα δεδομένα για να τα επεξεργαστούμε
        dff = pca.fit_transform(yeast_data)

        # Τρέχουμε το kmeans για X clusters
        kmeans = KMeans(n_clusters=numberOfClusters)

        # Οι προβλέψεις για τα δεδομένα
        label = kmeans.fit_predict(dff)

        # Getting unique labels
        u_labels = np.unique(label)

        # Εκτυπώνουμε τα clusters που έχουν ανατεθεί σε κάθε παρατήρηση
        print("Τα clusters είναι: ", kmeans.labels_)

        # Εκτυπώνουμε την Inertia
        print(f"Η Inertia είναι για {numberOfClusters} clusters είναι: ", kmeans.inertia_)

        # Υπολογίζουμε το πλήθος του κάθε cluster
        unique, counts = np.unique(label, return_counts=True)
        counts = counts.reshape(1, numberOfClusters)

        # Φτιάχνουμε ενα data frame με τα μεγέθη απο κάθε cluster
        numOfClusters = []
        target_names = []
        y = 0
        while y < numberOfClusters:
            numOfClusters.append(f"Cluster {y + 1}")
            target_names.append(f"Cluster {y + 1}")
            y += 1
        countsClDf = pd.DataFrame(counts, columns=numOfClusters)

        # εκτυπώνουμε τα μεγέθη
        print("Το κάθε cluster έχει μέγεθος:")
        print(countsClDf)
        # Βρίσκουμε το κέντρο του κάθε cluster
        centroids = kmeans.cluster_centers_
        # Κατασκευάζουμε τα γραφήματα για τα clusters και το κάθε κέντρο
        plt.figure(figsize=(12, 8))
        for d, target_name in zip(u_labels, target_names):
            plt.scatter(dff[label == d, 0], dff[label == d, 1], alpha=.6, lw=2, label=target_name)

        plt.scatter(centroids[:, 0], centroids[:, 1], s=80, color="k")
        plt.legend(loc="best")
        plt.title(f"Ομαδοποίηση με {numberOfClusters} clusters")
        plt.show()

    # Υλοποίηση της επιλογής όλων
    def select_all():
        if chVar11.get() == 1:
            chVar1.set(1)
            chVar2.set(1)
            chVar3.set(1)
            chVar4.set(1)
            chVar5.set(1)
            chVar6.set(1)
            chVar7.set(1)
            chVar8.set(1)
            chVar9.set(1)
            chVar10.set(1)
        else:
            chVar1.set(0)
            chVar2.set(0)
            chVar3.set(0)
            chVar4.set(0)
            chVar5.set(0)
            chVar6.set(0)
            chVar7.set(0)
            chVar8.set(0)
            chVar9.set(0)
            chVar10.set(0)

    # Υλοποίηση της επιλογής όλων 2
    def select_all2():
        if chVar20.get() == 1:
            chVar12.set(1)
            chVar13.set(1)
            chVar14.set(1)
            chVar15.set(1)
            chVar16.set(1)
            chVar17.set(1)
            chVar18.set(1)
            chVar19.set(1)
        else:
            chVar12.set(0)
            chVar13.set(0)
            chVar14.set(0)
            chVar15.set(0)
            chVar16.set(0)
            chVar17.set(0)
            chVar18.set(0)
            chVar19.set(0)

    # Συνάρτηση εμφάνισης στατιστικών στοιχείων για τις επιλεγμένες κυτταρικές τοποθεσίες
    def stats_exe():
        yeastData1 = yeastData.set_index("ClassDis")
        if chVar1.get() == chVar2.get() == chVar3.get() == chVar4.get() == chVar5.get() == chVar6.get() == \
                chVar7.get() == chVar8.get() == chVar9.get() == chVar10.get() == 0:
            messagebox.showerror(title="Statistics Error", message="Πρέπει να επιλέξετε τουλάχιστον 1 στοιχείο")
        else:
            if chVar1.get() == 1:
                print("Για την κυτταρική τοποθεσία CYT(cytosolic or cytoskeletal) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["CYT"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["CYT"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["CYT"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["CYT"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["CYT"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["CYT"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)

            if chVar2.get() == 1:
                print("Για την κυτταρική τοποθεσία NUC(nuclear) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["NUC"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["NUC"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["NUC"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["NUC"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["NUC"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["NUC"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar3.get() == 1:
                print("Για την κυτταρική τοποθεσία MIT(mitochondrial) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["MIT"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["MIT"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["MIT"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["MIT"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["MIT"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["MIT"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar4.get() == 1:
                print("Για την κυτταρική τοποθεσία ME3(membrane protein, no N-terminal signal) "
                      "τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["ME3"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["ME3"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["ME3"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["ME3"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["ME3"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["ME3"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar5.get() == 1:
                print(
                    "Για την κυτταρική τοποθεσία ME2(membrane protein, uncleaved signal) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["ME2"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["ME2"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["ME2"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["ME2"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["ME2"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["ME2"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar6.get() == 1:
                print("Για την κυτταρική τοποθεσία ME1(membrane protein, cleaved signal) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["ME1"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["ME1"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["ME1"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["ME1"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["ME1"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["ME1"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar7.get() == 1:
                print("Για την κυτταρική τοποθεσία EXC(extracellular) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["EXC"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["EXC"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["EXC"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["EXC"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["EXC"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["EXC"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar8.get() == 1:
                print("Για την κυτταρική τοποθεσία VAC(vacuolar) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["VAC"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["VAC"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["VAC"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["VAC"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["VAC"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["VAC"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar9.get() == 1:
                print("Για την κυτταρική τοποθεσία POX(peroxisomal) τα στατιστικά στοιχεία είναι:")
                print()
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["POX"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["POX"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["POX"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["POX"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["POX"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["POX"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)
            if chVar10.get() == 1:
                print("Για την κυτταρική τοποθεσία ERL(endoplasmic reticulum lumen) τα στατιστικά στοιχεία είναι:")
                # Αριθμητικός Μέσος
                arithmitikosmesos(yeastData1.loc["ERL"], onomata2)

                # Μέση Τιμή
                meshtimh(yeastData1.loc["ERL"], onomata2)

                # Χαμηλή Μέση Τιμή
                lowmeshtimh(yeastData1.loc["ERL"], onomata2)

                # Υψηλή Μέση Τιμή
                highmeshtimh(yeastData1.loc["ERL"], onomata2)

                # Τυπική Απόκλιση
                tupap = tupikhapoklish(yeastData1.loc["ERL"], onomata2)

                # Διακύμανση
                dia = funcdiakimansh(yeastData1.loc["ERL"], onomata2)

                # Σχεδιασμός Τυπικής Απόκλισης
                sxediasmostupikhapoklish(tupap)

                # Σχεδιασμός Διακύμανσης
                sxediasmosdiakimansh(dia)

    # Συνάρτηση πληροφοριών για τα στατιστικά στοιχεία
    def stats_info():
        messagebox.showinfo(title="Statistics Info", message="Επιλέξτε για ποιες κυτταρικές τοποθεσίες θέλετε να "
                                                             "εμφανιστούν τα στατιστικά στοιχεία (Αριθμητικό Μέσο, "
                                                             "Μέση Τιμή, Χαμηλή Μέση Τιμή,  Υψηλή Μέση Τιμή, "
                                                             "Τυπική Απόκλιση του Δείγματος και Διακύμανση μαζί με "
                                                             "ραβδογράμματα για την Τυπική Απόκλιση και Διακύμανση")

    # Χρήση του Tkinter για την κατασκευή του GUI
    label1 = ttk.Label(root, text="Project 42", font=("Times", 14))
    label1.place(x=150, y=5)

    label2 = ttk.Label(root, text="Για το Τεστ (υπο 1,2,3) --->")
    label2.place(x=10, y=45)

    button1 = ttk.Button(root, text="Τεστ", command=upo_exe)
    button1.place(x=200, y=42)

    button3 = ttk.Button(root, text="Info", command=upo_info)
    button3.place(x=290, y=42)

    label3 = ttk.Label(root, text="Για καμπύλη inertia --->")
    label3.place(x=10, y=85)

    button2 = ttk.Button(root, text="Inertia", command=inertia_exe)
    button2.place(x=200, y=82)

    button4 = ttk.Button(root, text="Info", command=inertia_info)
    button4.place(x=290, y=82)

    label4 = ttk.Label(root, text="Ομαδοποίηση", font=("Times", 12))
    label4.place(x=150, y=130)

    label5 = ttk.Label(root, text="Επιλέξτε τον αριθμό cluster που επιθυμείτε:")
    label5.place(x=10, y=170)

    clusters = IntVar()
    clusters.set(3)
    numbers = []
    for i in range(2, 9):
        numbers.append(str(i))
    combobox1 = ttk.Combobox(root, textvariable=clusters, values=numbers, state="readonly")
    combobox1.place(x=250, y=170)

    label7 = ttk.Label(root, text="Στατιστικά Στοιχεία", font=("Times", 12))
    label7.place(x=130, y=370)

    label6 = ttk.Label(root, text="Επιλέξτε για ποια στοιχεία θέλετε να εμφανιστούν τα στατιστικά:")
    label6.place(x=10, y=400)

    label7 = ttk.Label(root, text="Επιλέξτε τις τιμές που θα συμμετέχουν στην ομαδοποίηση:")
    label7.place(x=10, y=200)

    chVar1 = IntVar()
    chVar1.set(0)
    checkbox1 = ttk.Checkbutton(root, text="CYT(cytosolic or cytoskeletal)", variable=chVar1, onvalue=1, offvalue=0)
    checkbox1.place(x=30, y=430)

    chVar2 = IntVar()
    chVar2.set(0)
    checkbox2 = ttk.Checkbutton(root, text="NUC(nuclear)", variable=chVar2, onvalue=1, offvalue=0)
    checkbox2.place(x=30, y=460)

    chVar3 = IntVar()
    chVar3.set(0)
    checkbox3 = ttk.Checkbutton(root, text="MIT(mitochondrial)", variable=chVar3, onvalue=1, offvalue=0)
    checkbox3.place(x=30, y=490)

    chVar4 = IntVar()
    chVar4.set(0)
    checkbox4 = ttk.Checkbutton(root, text="ME3(membrane protein, no N-terminal signal)", variable=chVar4, onvalue=1,
                                offvalue=0)
    checkbox4.place(x=30, y=520)

    chVar5 = IntVar()
    chVar5.set(0)
    checkbox5 = ttk.Checkbutton(root, text="ME2(membrane protein, uncleaved signal)", variable=chVar5, onvalue=1,
                                offvalue=0)
    checkbox5.place(x=30, y=550)

    chVar6 = IntVar()
    chVar6.set(0)
    checkbox6 = ttk.Checkbutton(root, text="ME1(membrane protein, cleaved signal)", variable=chVar6, onvalue=1,
                                offvalue=0)
    checkbox6.place(x=30, y=580)

    chVar7 = IntVar()
    chVar7.set(0)
    checkbox7 = ttk.Checkbutton(root, text="EXC(extracellular)", variable=chVar7, onvalue=1, offvalue=0)
    checkbox7.place(x=30, y=610)

    chVar8 = IntVar()
    chVar8.set(0)
    checkbox8 = ttk.Checkbutton(root, text="VAC(vacuolar)", variable=chVar8, onvalue=1, offvalue=0)
    checkbox8.place(x=30, y=640)

    chVar9 = IntVar()
    chVar9.set(0)
    checkbox9 = ttk.Checkbutton(root, text="POX(peroxisomal)", variable=chVar9, onvalue=1, offvalue=0)
    checkbox9.place(x=30, y=670)

    chVar10 = IntVar()
    chVar10.set(0)
    checkbox10 = ttk.Checkbutton(root, text="ERL(endoplasmic reticulum lumen)", variable=chVar10, onvalue=1, offvalue=0)
    checkbox10.place(x=30, y=700)

    chVar11 = IntVar()
    chVar11.set(0)
    checkbox11 = ttk.Checkbutton(root, text="Select All", variable=chVar11, onvalue=1, offvalue=0, command=select_all)
    checkbox11.place(x=30, y=730)

    chVar12 = IntVar()
    chVar12.set(1)
    checkbox12 = ttk.Checkbutton(root, text="mcg", variable=chVar12, onvalue=1, offvalue=0)
    checkbox12.place(x=30, y=230)

    chVar13 = IntVar()
    chVar13.set(1)
    checkbox13 = ttk.Checkbutton(root, text="gvh", variable=chVar13, onvalue=1, offvalue=0)
    checkbox13.place(x=150, y=230)

    chVar14 = IntVar()
    chVar14.set(1)
    checkbox14 = ttk.Checkbutton(root, text="alm", variable=chVar14, onvalue=1, offvalue=0)
    checkbox14.place(x=270, y=230)

    chVar15 = IntVar()
    chVar15.set(1)
    checkbox15 = ttk.Checkbutton(root, text="mit", variable=chVar15, onvalue=1, offvalue=0)
    checkbox15.place(x=30, y=260)

    chVar16 = IntVar()
    chVar16.set(1)
    checkbox16 = ttk.Checkbutton(root, text="erl", variable=chVar16, onvalue=1, offvalue=0)
    checkbox16.place(x=150, y=260)

    chVar17 = IntVar()
    chVar17.set(1)
    checkbox17 = ttk.Checkbutton(root, text="pox", variable=chVar17, onvalue=1, offvalue=0)
    checkbox17.place(x=270, y=260)

    chVar18 = IntVar()
    chVar18.set(1)
    checkbox18 = ttk.Checkbutton(root, text="vac", variable=chVar18, onvalue=1, offvalue=0)
    checkbox18.place(x=30, y=290)

    chVar19 = IntVar()
    chVar19.set(1)
    checkbox19 = ttk.Checkbutton(root, text="nuc", variable=chVar19, onvalue=1, offvalue=0)
    checkbox19.place(x=150, y=290)

    chVar20 = IntVar()
    chVar20.set(1)
    checkbox20 = ttk.Checkbutton(root, text="Select All", variable=chVar20, onvalue=1, offvalue=0, command=select_all2)
    checkbox20.place(x=270, y=290)

    button5 = ttk.Button(root, text="Εκτέλεση Cluster", width=30, command=cluster_exe)
    button5.place(x=30, y=330)

    button6 = ttk.Button(root, text="Info", command=cluster_info)
    button6.place(x=270, y=330)

    button7 = ttk.Button(root, text="Εκτέλεση", width=30, command=stats_exe)
    button7.place(x=30, y=770)

    button8 = ttk.Button(root, text="Info", command=stats_info)
    button8.place(x=270, y=770)

    # Διαβάζει απο το αρχείο yeast.data τα στοιχεία και τους βάζει τον τίτλο τους
    yeastData = pd.read_fwf(r"yeast.data", header=None,
                            names=["Sequence Name", "mcg", "gvh", "alm", "mit", "erl", "pox", "vac", "nuc", "ClassDis"])

    # Διαγράφει την πρώτη στήλη
    del yeastData["Sequence Name"]

    print(yeastData)

    root.mainloop()


if __name__ == '__main__':
    main()
