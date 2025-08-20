import os

# HTML内容
html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>企业信用评分系统</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>企业信用评分系统</h1>
        
        <!-- 基本信息部分 -->
        <section class="company-info">
            <h2>企业基本信息</h2>
            <div class="info-group">
                <label>公司名称：</label>
                <input type="text" id="companyName">
            </div>
            <div class="info-group">
                <label>注册资本：</label>
                <input type="number" id="registeredCapital">
            </div>
            <div class="info-group">
                <label>法人代表：</label>
                <input type="text" id="legalPerson">
            </div>
            
            <!-- 专利信息 -->
            <div class="patent-info">
                <label>发明专利数量：</label>
                <input type="number" id="patentCount">
                <button onclick="addPatentInfo()">添加专利信息</button>
                <div id="patentList"></div>
            </div>
        </section>

        <!-- 评分卡部分 -->
        <section class="score-card">
            <h2>信用评分卡</h2>
            <div class="score-items">
                <div class="score-item">
                    <label>
                        <input type="checkbox" id="policyCompliance">
                        满足我行授信政策指引 (30分)
                    </label>
                </div>
                <div class="score-item">
                    <label>
                        <input type="checkbox" id="creditHistory">
                        征信近60个月无逾期 (10分)
                    </label>
                </div>
                <div class="score-item">
                    <label>
                        <input type="checkbox" id="supplyChain">
                        使用我行供应链结算产品 (20分)
                    </label>
                </div>
                <div class="score-item">
                    <label>
                        <input type="checkbox" id="settlement">
                        使用我行结算产品 (20分)
                    </label>
                </div>
            </div>

            <!-- 财务指标部分 -->
            <div class="financial-info">
                <h3>财务指标信息</h3>
                <div class="score-item">
                    <label>
                        <input type="checkbox" id="hasFinancialData" onchange="toggleFinancialData()">
                        包含Wind财务数据 (20分)
                    </label>
                </div>
                <div id="financialMetrics" style="display: none;">
                    <div class="metrics-grid">
                        <div class="metric-item">
                            <label>资产负债率：</label>
                            <input type="number" id="debtRatio" step="0.01">
                            <span>%</span>
                        </div>
                        <div class="metric-item">
                            <label>流动比率：</label>
                            <input type="number" id="currentRatio" step="0.01">
                        </div>
                        <div class="metric-item">
                            <label>净资产收益率：</label>
                            <input type="number" id="roe" step="0.01">
                            <span>%</span>
                        </div>
                        <div class="metric-item">
                            <label>营业收入增长率：</label>
                            <input type="number" id="revenueGrowth" step="0.01">
                            <span>%</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 风险提示 -->
            <div class="risk-warning">
                <label>
                    <input type="checkbox" id="hasRisk">
                    存在被执行人信息或破产信息
                </label>
            </div>
        </section>

        <button onclick="calculateScore()" class="calculate-btn">计算评分</button>

        <!-- 评分结果 -->
        <section class="result" id="resultSection" style="display: none;">
            <h2>评分结果</h2>
            <div id="totalScore"></div>
            <div id="recommendation"></div>
        </section>
    </div>
    <script src="script1.js"></script>
</body>
</html>"""

# CSS内容
css_content = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Microsoft YaHei', sans-serif;
    line-height: 1.6;
    background-color: #f5f5f5;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
}

h2 {
    color: #444;
    margin-bottom: 20px;
}

.info-group {
    margin-bottom: 15px;
}

label {
    display: inline-block;
    width: 120px;
    margin-right: 10px;
}

input[type="text"],
input[type="number"] {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    width: 200px;
}

.score-card {
    margin-top: 30px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 6px;
}

.score-item {
    margin-bottom: 10px;
}

.risk-warning {
    margin-top: 20px;
    padding: 10px;
    background-color: #fff3f3;
    border-left: 4px solid #ff4444;
}

.calculate-btn {
    display: block;
    width: 200px;
    margin: 30px auto;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.calculate-btn:hover {
    background-color: #45a049;
}

.result {
    margin-top: 30px;
    padding: 20px;
    background-color: #e8f5e9;
    border-radius: 6px;
}

#totalScore {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 15px;
}

#recommendation {
    padding: 15px;
    background-color: #fff;
    border-radius: 4px;
}

.patent-info {
    margin-top: 20px;
}

#patentList {
    margin-top: 10px;
}

.patent-item {
    padding: 10px;
    background-color: #f5f5f5;
    margin-bottom: 5px;
    border-radius: 4px;
}

.financial-info {
    margin-top: 20px;
    padding: 15px;
    background-color: #f0f7ff;
    border-radius: 6px;
    border-left: 4px solid #1976d2;
}

.financial-info h3 {
    color: #1976d2;
    margin-bottom: 15px;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-top: 15px;
}

.metric-item {
    display: flex;
    align-items: center;
    gap: 10px;
}

.metric-item input {
    width: 100px;
}

.metric-item span {
    color: #666;
}

.financial-summary {
    margin-top: 15px;
    padding: 10px;
    background-color: #e3f2fd;
    border-radius: 4px;
}
"""

# JavaScript内容
js_content = """// 专利信息列表
let patents = [];

// 添加专利信息
function addPatentInfo() {
    const patentInfo = prompt('请输入专利信息（名称、专利号等）：');
    if (patentInfo) {
        patents.push(patentInfo);
        updatePatentList();
    }
}

// 更新专利列表显示
function updatePatentList() {
    const patentList = document.getElementById('patentList');
    patentList.innerHTML = patents.map(patent => 
        `<div class="patent-item">${patent}</div>`
    ).join('');
}

// 切换财务数据显示
function toggleFinancialData() {
    const hasData = document.getElementById('hasFinancialData').checked;
    const metricsDiv = document.getElementById('financialMetrics');
    metricsDiv.style.display = hasData ? 'block' : 'none';
    
    if (!hasData) {
        document.getElementById('debtRatio').value = '';
        document.getElementById('currentRatio').value = '';
        document.getElementById('roe').value = '';
        document.getElementById('revenueGrowth').value = '';
    }
}

// 获取财务指标评估
function getFinancialAssessment() {
    const hasData = document.getElementById('hasFinancialData').checked;
    if (!hasData) {
        return {
            score: 0,
            summary: '未提供财务数据'
        };
    }

    const metrics = {
        debtRatio: parseFloat(document.getElementById('debtRatio').value) || 0,
        currentRatio: parseFloat(document.getElementById('currentRatio').value) || 0,
        roe: parseFloat(document.getElementById('roe').value) || 0,
        revenueGrowth: parseFloat(document.getElementById('revenueGrowth').value) || 0
    };

    let assessment = [];
    let score = 20; // 初始满分20分
    
    // 资产负债率评估（一般认为<70%较好）
    if (metrics.debtRatio < 70) {
        assessment.push('资产负债率处于合理水平');
    } else {
        assessment.push('资产负债率偏高');
        score -= 5;
    }

    // 流动比率评估（一般>1.5较好）
    if (metrics.currentRatio > 1.5) {
        assessment.push('流动性良好');
    } else {
        assessment.push('流动性需要关注');
        score -= 5;
    }

    // ROE评估（一般>10%较好）
    if (metrics.roe > 10) {
        assessment.push('盈利能力强');
    } else {
        assessment.push('盈利能力有待提升');
        score -= 5;
    }

    // 收入增长率评估（>0为正向）   
    if (metrics.revenueGrowth > 0) {
        assessment.push('营收呈增长趋势');
    } else {
        assessment.push('营收增长承压');
        score -= 5;
    }

    return {
        score: score,
        summary: assessment.join('；')
    };
}

// 获取营销话术
function getMarketingScript(score, financialAssessment) {
    const companyName = document.getElementById('companyName').value || '贵司';
    
    if (score >= 80) {
        return {
            title: '🌟 优质客户合作建议',
            scripts: [
                `尊敬的${companyName}：`,
                '基于您的优质信用记录和稳健经营，我们诚挚建议：',
                `1. 可为您提供最高${Math.floor(score * 100)}万元的意向性授信额度`,
                '2. 专享供应链融资优惠利率，最低可至LPR-15BP',
                '3. 配备专属金融顾问，提供一对一定制服务',
                '4. 优先办理银行承兑汇票、国际信用证等贸易融资业务',
                '5. 可提供跨境金融、资金管理等综合性金融解决方案',
                '6. 享受本行VIP客户绿色通道服务'
            ]
        };
    } else if (score >= 60) {
        return {
            title: '🌱 成长客户合作建议',
            scripts: [
                `尊敬的${companyName}：`,
                '看到您的企业发展潜力，我们建议：',
                '1. 提供灵活的供应链融资方案，助力企业扩大经营',
                '2. 优先考虑订单融资、应收账款融资等业务',
                '3. 提供结算账户优惠服务，降低财务成本',
                '4. 为您定制个性化融资方案',
                '5. 建议开展现金管理业务，提升资金使用效率',
                '6. 提供企业财务管理咨询服务'
            ]
        };
    } else {
        return {
            title: '💪 提升建议',
            scripts: [
                `尊敬的${companyName}：`,
                '为助力您的业务更好发展，我们建议：',
                '1. 协助完善企业财务管理体系',
                '2. 加强与核心企业的业务合作关系',
                '3. 通过我行结算服务建立良好的信用记录',
                '4. 提供专业建议帮助优化资产负债结构',
                '5. 从小额结算业务开始，逐步建立合作基础',
                '6. 定期提供行业分析和金融市场资讯'
            ]
        };
    }
}

// 计算评分
function calculateScore() {
    let totalScore = 0;
    let failureReasons = [];
    const companyName = document.getElementById('companyName').value;

    if (!companyName) {
        alert('请输入公司名称！');
        return;
    }

    // 检查授信政策
    if (document.getElementById('policyCompliance').checked) {
        totalScore += 30;
    } else {
        failureReasons.push('不满足授信政策指引');
    }

    // 检查征信历史
    if (document.getElementById('creditHistory').checked) {
        totalScore += 10;
    } else {
        failureReasons.push('征信记录存在逾期');
    }

    // 检查供应链结算
    if (document.getElementById('supplyChain').checked) {
        totalScore += 20;   
    } else {
        failureReasons.push('未使用供应链结算产品');
    }

    // 检查结算产品
    if (document.getElementById('settlement').checked) {
        totalScore += 20;
    } else {
        failureReasons.push('未使用我行结算产品');
    }

    // 添加财务评分
    const financialAssessment = getFinancialAssessment();
    totalScore += financialAssessment.score;
    
    if (financialAssessment.score === 0) {
        failureReasons.push('未提供财务数据');
    }

    // 检查风险信息
    if (document.getElementById('hasRisk').checked) {
        totalScore = 0;
        failureReasons.push('存在被执行人信息或破产信息');
    }

    // 显示结果
    const resultSection = document.getElementById('resultSection');
    const totalScoreDiv = document.getElementById('totalScore');
    const recommendationDiv = document.getElementById('recommendation');

    resultSection.style.display = 'block';
    
    // 根据分数设置不同的样式
    let scoreClass = '';
    if (totalScore >= 80) scoreClass = 'score-high';
    else if (totalScore >= 60) scoreClass = 'score-medium';
    else scoreClass = 'score-low';
    
    totalScoreDiv.innerHTML = `
        <div class="score-circle ${scoreClass}">
            <span class="score-number">${totalScore}</span>
            <span class="score-label">分</span>
        </div>
    `;

    const marketingScript = getMarketingScript(totalScore, financialAssessment);

    if (totalScore >= 60) {
        recommendationDiv.innerHTML = `
            <div class="result-card success">
                <h3>推荐产品</h3>
                <ul class="product-list">
                    <li><i class="icon">💰</i>供应链融资</li>
                    <li><i class="icon">💳</i>流动资金贷款</li>
                    <li><i class="icon">📄</i>银行承兑汇票</li>
                </ul>
                <div class="financial-summary">
                    <h4>财务评估：</h4>
                    <p>${financialAssessment.summary}</p>
                </div>
                <div class="marketing-suggestions">
                    <h4>${marketingScript.title}</h4>
                    <ul>
                        ${marketingScript.scripts.map(script => `<li>${script}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    } else {
        recommendationDiv.innerHTML = `
            <div class="result-card warning">
                <h3>未通过原因：</h3>
                <ul class="failure-reasons">
                    ${failureReasons.map(reason => `<li>${reason}</li>`).join('')}
                </ul>
                <div class="marketing-suggestions">
                    <h4>${marketingScript.title}</h4>
                    <ul>
                        ${marketingScript.scripts.map(script => `<li>${script}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    }

    // 平滑滚动到结果区域
    resultSection.scrollIntoView({ behavior: 'smooth' });
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    // 添加输入验证
    document.getElementById('companyName').addEventListener('input', function(e) {
        if (e.target.value.length > 50) {
            e.target.value = e.target.value.slice(0, 50);
            alert('公司名称不能超过50个字符');
        }
    });
});"""

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建文件
def create_file(filename, content):
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已创建文件: {filename}")

# 创建所需的文件
create_file('company_credit.html', html_content)
create_file('styles.css', css_content)
create_file('script1.js', js_content)

print("\n所有文件已创建完成，现在可以运行 Untitled-1.py 了") 