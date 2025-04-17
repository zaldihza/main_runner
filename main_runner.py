import time
import sys
import os

# Import modul-modul dari assignment sebelumnya
# Assignment 1
from assignment_1 import a_star_search as a1_astar, greedy_best_first_search as a1_gbfs
# Assignment 2
from assignment_2 import a_star_search as a2_astar, greedy_best_first_search as a2_gbfs
# Assignment 3
from assignment_3 import a_star_search as a3_astar, greedy_best_first_search as a3_gbfs
# Assignment 4
from assignment_4 import a_star_search as a4_astar, greedy_best_first_search as a4_gbfs

def run_assignment_1():
    """Jalankan dan bandingkan algoritma untuk Assignment 1: City Navigation"""
    print("Running Assignment 1: City Navigation")
    
    # Data kota dan jalan
    cities = {
        "A": (0, 0),
        "B": (2, 1),
        "C": (4, 2),
        "D": (5, 5),
        "E": (1, 4)
    }
    
    roads = {
        "A": ["B", "E"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"],
        "E": ["A", "D"]
    }
    
    # Jalankan kedua algoritma
    start_city, goal_city = "A", "D"
    
    # A* Search
    a_star_path, a_star_visited, a_star_time = a1_astar(roads, cities, start_city, goal_city)
    
    # Greedy Best-First Search
    gbfs_path, gbfs_visited, gbfs_time = a1_gbfs(roads, cities, start_city, goal_city)
    
    # Return hasil untuk perbandingan
    return {
        'a_star_time': a_star_time,
        'gbfs_time': gbfs_time,
        'a_star_nodes': a_star_visited,
        'gbfs_nodes': gbfs_visited
    }

def run_assignment_2():
    """Jalankan dan bandingkan algoritma untuk Assignment 2: Emergency Response"""
    print("Running Assignment 2: Emergency Response")
    
    # Contoh peta kota untuk ambulan
    city_map = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "S", ".", ".", "T", "T", ".", ".", "."],
        [".", ".", ".", ".", "T", ".", ".", ".", "."],
        [".", "T", "T", "T", "T", ".", "T", "T", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "T", "T", ".", "T", "T", ".", "."],
        [".", ".", ".", ".", ".", ".", "T", ".", "."],
        [".", "T", ".", "T", "T", ".", ".", "H", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    
    # Temukan posisi ambulan dan rumah sakit
    start_pos = None
    goal_pos = None
    
    for i in range(len(city_map)):
        for j in range(len(city_map[0])):
            if city_map[i][j] == "S":
                start_pos = (i, j)
            elif city_map[i][j] == "H":
                goal_pos = (i, j)
    
    # Jalankan kedua algoritma
    # A* Search
    a_star_path, a_star_visited, a_star_time = a2_astar(city_map, start_pos, goal_pos)
    
    # Greedy Best-First Search
    gbfs_path, gbfs_visited, gbfs_time = a2_gbfs(city_map, start_pos, goal_pos)
    
    # Return hasil untuk perbandingan
    return {
        'a_star_time': a_star_time,
        'gbfs_time': gbfs_time,
        'a_star_nodes': a_star_visited,
        'gbfs_nodes': gbfs_visited
    }

def run_assignment_3():
    """Jalankan dan bandingkan algoritma untuk Assignment 3: Food Delivery"""
    print("Running Assignment 3: Food Delivery")
    
    # Import DeliveryMap class
    from assignment_3 import DeliveryMap
    
    # Buat peta pengantaran makanan
    delivery_map = DeliveryMap(15, 15)
    delivery_map.generate_random_map()
    
    # Ambil restoran dan pelanggan pertama
    if len(delivery_map.restaurants) > 0 and len(delivery_map.customers) > 0:
        restaurant_name = list(delivery_map.restaurants.keys())[0]
        customer_name = list(delivery_map.customers.keys())[0]
        
        restaurant_pos = delivery_map.restaurants[restaurant_name]
        customer_pos = delivery_map.customers[customer_name]
        
        # Jalankan kedua algoritma
        # A* Search
        a_star_path, a_star_visited, a_star_time = a3_astar(delivery_map, restaurant_pos, customer_pos)
        
        # Greedy Best-First Search
        gbfs_path, gbfs_visited, gbfs_time = a3_gbfs(delivery_map, restaurant_pos, customer_pos)
        
        # Return hasil untuk perbandingan
        return {
            'a_star_time': a_star_time,
            'gbfs_time': gbfs_time,
            'a_star_nodes': a_star_visited,
            'gbfs_nodes': gbfs_visited
        }
    
    return {
        'a_star_time': 0,
        'gbfs_time': 0,
        'a_star_nodes': 0,
        'gbfs_nodes': 0
    }

def run_assignment_4():
    """Jalankan dan bandingkan algoritma untuk Assignment 4: Drone Navigation"""
    print("Running Assignment 4: Drone Navigation")
    
    # Import TerrainMap class
    from assignment_4 import TerrainMap
    
    # Buat peta terrain
    terrain_map = TerrainMap(20, 20)
    terrain_map.generate_random_terrain()
    
    # Posisi awal dan tujuan sudah diatur dalam generate_random_terrain()
    # Jadi tidak perlu set_start dan set_goal di sini
    
    # Jalankan kedua algoritma
    # A* Search
    a_star_path, a_star_visited, a_star_time = a4_astar(terrain_map)
    
    # Greedy Best-First Search
    gbfs_path, gbfs_visited, gbfs_time = a4_gbfs(terrain_map)
    
    # Return hasil untuk perbandingan
    return {
        'a_star_time': a_star_time,
        'gbfs_time': gbfs_time,
        'a_star_nodes': a_star_visited,
        'gbfs_nodes': gbfs_visited
    }

def format_results(results):
    """Format hasil perbandingan untuk ditampilkan"""
    print("\nPerbandingan Algoritma:")
    print("-" * 60)
    print(f"{'Algorithm':<15} {'Time (ms)':<15} {'Nodes Visited':<15}")
    print("-" * 60)
    print(f"{'A* Search':<15} {results['a_star_time']*1000:<15.2f} {results['a_star_nodes']:<15}")
    print(f"{'Greedy BFS':<15} {results['gbfs_time']*1000:<15.2f} {results['gbfs_nodes']:<15}")
    print("-" * 60)
    
    # Hitung persentase perbedaan
    time_diff_percent = ((results['gbfs_time'] - results['a_star_time']) / results['a_star_time']) * 100
    nodes_diff_percent = ((results['gbfs_nodes'] - results['a_star_nodes']) / results['a_star_nodes']) * 100
    
    print(f"\nPersentase perbedaan waktu: {time_diff_percent:.2f}%")
    print(f"Persentase perbedaan jumlah node: {nodes_diff_percent:.2f}%")
    
    # Kesimpulan
    if results['a_star_time'] < results['gbfs_time']:
        print("\nA* Search lebih cepat dari Greedy Best-First Search")
    else:
        print("\nGreedy Best-First Search lebih cepat dari A* Search")
        
    if results['a_star_nodes'] < results['gbfs_nodes']:
        print("A* Search mengunjungi lebih sedikit node dari Greedy Best-First Search")
    else:
        print("Greedy Best-First Search mengunjungi lebih sedikit node dari A* Search")

def save_results_to_file(results, assignment_name):
    """Menyimpan hasil ke file CSV"""
    import csv
    
    filename = f"comparison_results_{assignment_name}.csv"
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['assignment', 'a_star_time', 'gbfs_time', 'a_star_nodes', 'gbfs_nodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'assignment': assignment_name,
            'a_star_time': results['a_star_time'],
            'gbfs_time': results['gbfs_time'],
            'a_star_nodes': results['a_star_nodes'],
            'gbfs_nodes': results['gbfs_nodes']
        })
    
    print(f"\nHasil tersimpan ke file: {filename}")

def create_comparison_chart(assignment_results):
    """Membuat grafik perbandingan dari semua assignment"""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        assignments = list(assignment_results.keys())
        x = np.arange(len(assignments))
        width = 0.35
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
        
        # Plot waktu eksekusi
        a_star_times = [assignment_results[a]['a_star_time']*1000 for a in assignments]
        gbfs_times = [assignment_results[a]['gbfs_time']*1000 for a in assignments]
        
        rects1 = ax1.bar(x - width/2, a_star_times, width, label='A* Search')
        rects2 = ax1.bar(x + width/2, gbfs_times, width, label='Greedy BFS')
        
        ax1.set_title('Perbandingan Waktu Eksekusi (ms)')
        ax1.set_xticks(x)
        ax1.set_xticklabels(assignments)
        ax1.legend()
        
        # Plot jumlah node yang dikunjungi
        a_star_nodes = [assignment_results[a]['a_star_nodes'] for a in assignments]
        gbfs_nodes = [assignment_results[a]['gbfs_nodes'] for a in assignments]
        
        rects3 = ax2.bar(x - width/2, a_star_nodes, width, label='A* Search')
        rects4 = ax2.bar(x + width/2, gbfs_nodes, width, label='Greedy BFS')
        
        ax2.set_title('Perbandingan Jumlah Node yang Dikunjungi')
        ax2.set_xticks(x)
        ax2.set_xticklabels(assignments)
        ax2.legend()
        
        plt.tight_layout()
        plt.savefig('algorithm_comparison.png')
        plt.close()
        
        print("\nGrafik perbandingan tersimpan ke file: algorithm_comparison.png")
    except ImportError:
        print("\nMatplotlib tidak tersedia. Grafik tidak dibuat.")

def main():
    """Fungsi utama program"""
    print("Program Perbandingan Algoritma A* dan Greedy Best-First Search\n")
    
    # Dictionary untuk menyimpan hasil semua assignment
    all_results = {}
    
    # Assignment 1
    print("\n" + "="*60)
    results_1 = run_assignment_1()
    format_results(results_1)
    save_results_to_file(results_1, "City Navigation")
    all_results["City Navigation"] = results_1
    
    # Assignment 2
    print("\n" + "="*60)
    results_2 = run_assignment_2()
    format_results(results_2)
    save_results_to_file(results_2, "Emergency Response")
    all_results["Emergency Response"] = results_2
    
    # Assignment 3
    print("\n" + "="*60)
    results_3 = run_assignment_3()
    format_results(results_3)
    save_results_to_file(results_3, "Food Delivery")
    all_results["Food Delivery"] = results_3
    
    # Assignment 4
    print("\n" + "="*60)
    results_4 = run_assignment_4()
    format_results(results_4)
    save_results_to_file(results_4, "Drone Navigation")
    all_results["Drone Navigation"] = results_4
    
    # Buat grafik perbandingan
    create_comparison_chart(all_results)
    
    print("\n" + "="*60)
    print("Program selesai!")

if __name__ == "__main__":
    main()