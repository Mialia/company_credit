// 专利信息列表
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
});