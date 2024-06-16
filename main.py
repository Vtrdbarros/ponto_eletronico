import sys
sys.path.append('C:\\Users\\Yagob\\OneDrive\\Documentos\\deVtr\\ponto_eletronico')

print("Starting application")

try:
    from app import create_app
    print("Imported create_app successfully")
except ImportError as e:
    print(f"Error importing create_app: {e}")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
