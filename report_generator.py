"""
Générateur de rapports
Crée des rapports exportables en PDF, CSV, etc.
"""

import pandas as pd
from datetime import datetime
import io

class ReportGenerator:
    def __init__(self, df, analysis_results=None):
        """
        Initialise le générateur de rapports
        
        Parameters:
        df (pd.DataFrame): Données analysées
        analysis_results (dict): Résultats des analyses statistiques
        """
        self.df = df
        self.analysis_results = analysis_results or {}
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def generate_summary_report(self):
        """Génère un rapport résumé en texte"""
        report = []
        report.append("=" * 60)
        report.append("RAPPORT D'ANALYSE - SOCIAL MEDIA ANALYTICS PRO")
        report.append("=" * 60)
        report.append(f"\nDate: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        report.append(f"Nombre de données: {len(self.df)} entrées")
        
        # Informations générales
        report.append("\n" + "=" * 60)
        report.append("1. STATISTIQUES GÉNÉRALES")
        report.append("=" * 60)
        
        if 'platform' in self.df.columns:
            platforms = self.df['platform'].unique()
            report.append(f"\nPlateformes analysées: {', '.join(platforms)}")
            report.append(f"Nombre de plateformes: {len(platforms)}")
        
        # Métriques clés
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        
        if 'likes' in numeric_cols:
            report.append(f"\nTotal de likes: {self.df['likes'].sum():,.0f}")
            report.append(f"Moyenne de likes: {self.df['likes'].mean():.2f}")
            report.append(f"Médiane de likes: {self.df['likes'].median():.2f}")
        
        if 'engagement_rate' in numeric_cols:
            report.append(f"\nTaux d'engagement moyen: {self.df['engagement_rate'].mean():.2f}%")
            report.append(f"Taux d'engagement médian: {self.df['engagement_rate'].median():.2f}%")
        
        # Résultats des tests
        if self.analysis_results:
            report.append("\n" + "=" * 60)
            report.append("2. RÉSULTATS DES TESTS STATISTIQUES")
            report.append("=" * 60)
            
            for test_name, result in self.analysis_results.items():
                report.append(f"\n{test_name.upper().replace('_', ' ')}")
                report.append("-" * 40)
                
                if 'interpretation' in result:
                    report.append(result['interpretation'])
                
                if 'p_value' in result:
                    report.append(f"P-value: {result['p_value']:.4f}")
                    report.append(f"Significatif: {'Oui' if result.get('significant', False) else 'Non'}")
        
        # Comparaison par plateforme
        if 'platform' in self.df.columns and 'engagement_rate' in self.df.columns:
            report.append("\n" + "=" * 60)
            report.append("3. COMPARAISON PAR PLATEFORME")
            report.append("=" * 60)
            
            platform_stats = self.df.groupby('platform').agg({
                'engagement_rate': ['mean', 'median', 'std'],
                'likes': ['sum', 'mean']
            }).round(2)
            
            for platform in self.df['platform'].unique():
                platform_data = self.df[self.df['platform'] == platform]
                report.append(f"\n{platform}:")
                report.append(f"  - Engagement moyen: {platform_data['engagement_rate'].mean():.2f}%")
                report.append(f"  - Total likes: {platform_data['likes'].sum():,.0f}")
                report.append(f"  - Nombre de posts: {len(platform_data)}")
        
        # Recommandations
        report.append("\n" + "=" * 60)
        report.append("4. RECOMMANDATIONS")
        report.append("=" * 60)
        
        if 'platform' in self.df.columns and 'engagement_rate' in self.df.columns:
            best_platform = self.df.groupby('platform')['engagement_rate'].mean().idxmax()
            worst_platform = self.df.groupby('platform')['engagement_rate'].mean().idxmin()
            
            report.append(f"\n✅ Meilleure plateforme: {best_platform}")
            report.append(f"   → Continuez à investir sur cette plateforme")
            
            report.append(f"\n⚠️  Plateforme à améliorer: {worst_platform}")
            report.append(f"   → Analysez ce qui fonctionne sur {best_platform}")
        
        report.append("\n" + "=" * 60)
        report.append("FIN DU RAPPORT")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def export_to_csv(self):
        """Exporte les données en CSV"""
        output = io.StringIO()
        self.df.to_csv(output, index=False)
        return output.getvalue()
    
    def export_summary_to_csv(self):
        """Exporte un résumé en CSV"""
        summary_data = []
        
        if 'platform' in self.df.columns:
            for platform in self.df['platform'].unique():
                platform_data = self.df[self.df['platform'] == platform]
                
                row = {
                    'Plateforme': platform,
                    'Nombre de posts': len(platform_data),
                }
                
                numeric_cols = platform_data.select_dtypes(include=['number']).columns
                for col in numeric_cols:
                    row[f'{col}_moyenne'] = platform_data[col].mean()
                    row[f'{col}_total'] = platform_data[col].sum()
                
                summary_data.append(row)
        
        summary_df = pd.DataFrame(summary_data)
        output = io.StringIO()
        summary_df.to_csv(output, index=False)
        return output.getvalue()
    
    def export_test_results_to_csv(self):
        """Exporte les résultats des tests en CSV"""
        if not self.analysis_results:
            return "Test,Résultat\nAucun test effectué,N/A\n"
        
        results_data = []
        
        for test_name, result in self.analysis_results.items():
            row = {
                'Test': test_name.replace('_', ' ').title(),
            }
            
            if 'p_value' in result:
                row['P-value'] = result['p_value']
            if 'significant' in result:
                row['Significatif'] = 'Oui' if result['significant'] else 'Non'
            if 'statistic' in result:
                row['Statistique'] = result['statistic']
            if 'correlation' in result:
                row['Corrélation'] = result['correlation']
            if 'interpretation' in result:
                row['Interprétation'] = result['interpretation']
            
            results_data.append(row)
        
        results_df = pd.DataFrame(results_data)
        output = io.StringIO()
        results_df.to_csv(output, index=False)
        return output.getvalue()
    
    def generate_html_report(self, is_premium=False):
        """Génère un rapport HTML stylisé"""
        html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport d'Analyse - Social Media Analytics Pro</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #764ba2;
            margin-top: 30px;
        }}
        .metric {{
            display: inline-block;
            background: #f8f9fa;
            padding: 15px 25px;
            margin: 10px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        .metric-value {{
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }}
        .metric-label {{
            font-size: 14px;
            color: #6c757d;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }}
        th {{
            background: #667eea;
            color: white;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge-success {{
            background: #28a745;
            color: white;
        }}
        .badge-warning {{
            background: #ffc107;
            color: black;
        }}
        .badge-premium {{
            background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }}
        .footer {{
            margin-top: 40px;
            text-align: center;
            color: #6c757d;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Rapport d'Analyse Social Media</h1>
        <p><strong>Généré le:</strong> {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
        
        {"<span class='badge badge-premium'>👑 PREMIUM</span>" if is_premium else "<span class='badge badge-warning'>🆓 GRATUIT</span>"}
        
        <h2>📈 Statistiques Générales</h2>
        <div>
            <div class="metric">
                <div class="metric-value">{len(self.df)}</div>
                <div class="metric-label">Entrées de données</div>
            </div>
"""
        
        if 'platform' in self.df.columns:
            html += f"""
            <div class="metric">
                <div class="metric-value">{self.df['platform'].nunique()}</div>
                <div class="metric-label">Plateformes</div>
            </div>
"""
        
        if 'likes' in self.df.columns:
            html += f"""
            <div class="metric">
                <div class="metric-value">{self.df['likes'].sum():,.0f}</div>
                <div class="metric-label">Total de likes</div>
            </div>
            <div class="metric">
                <div class="metric-value">{self.df['likes'].mean():.0f}</div>
                <div class="metric-label">Moyenne de likes</div>
            </div>
"""
        
        if 'engagement_rate' in self.df.columns:
            html += f"""
            <div class="metric">
                <div class="metric-value">{self.df['engagement_rate'].mean():.2f}%</div>
                <div class="metric-label">Taux d'engagement moyen</div>
            </div>
"""
        
        # Tableau par plateforme
        if 'platform' in self.df.columns and 'engagement_rate' in self.df.columns:
            html += """
        </div>
        
        <h2>🌐 Comparaison par Plateforme</h2>
        <table>
            <thead>
                <tr>
                    <th>Plateforme</th>
                    <th>Posts</th>
                    <th>Engagement Moyen</th>
                    <th>Total Likes</th>
                    <th>Performance</th>
                </tr>
            </thead>
            <tbody>
"""
            
            for platform in self.df['platform'].unique():
                platform_data = self.df[self.df['platform'] == platform]
                avg_engagement = platform_data['engagement_rate'].mean()
                total_likes = platform_data['likes'].sum() if 'likes' in platform_data.columns else 0
                
                performance = "🏆 Excellente" if avg_engagement > 5 else "✅ Bonne" if avg_engagement > 3 else "⚠️ À améliorer"
                
                html += f"""
                <tr>
                    <td><strong>{platform}</strong></td>
                    <td>{len(platform_data)}</td>
                    <td>{avg_engagement:.2f}%</td>
                    <td>{total_likes:,.0f}</td>
                    <td>{performance}</td>
                </tr>
"""
            
            html += """
            </tbody>
        </table>
"""
        
        # Résultats des tests
        if self.analysis_results:
            html += """
        <h2>🧪 Résultats des Tests Statistiques</h2>
"""
            
            for test_name, result in self.analysis_results.items():
                significant = result.get('significant', False)
                badge = '<span class="badge badge-success">Significatif</span>' if significant else '<span class="badge badge-warning">Non significatif</span>'
                
                html += f"""
        <div style="background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px;">
            <h3>{test_name.replace('_', ' ').title()} {badge}</h3>
"""
                
                if 'p_value' in result:
                    html += f"<p><strong>P-value:</strong> {result['p_value']:.4f}</p>"
                
                if 'interpretation' in result:
                    html += f"<p>{result['interpretation']}</p>"
                
                html += "</div>"
        
        html += """
        <div class="footer">
            <p>Généré par <strong>Social Media Analytics Pro</strong></p>
            <p>© 2024 - Tous droits réservés</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html
    
    def get_filename(self, extension):
        """Génère un nom de fichier avec timestamp"""
        return f"social_media_report_{self.timestamp}.{extension}"

