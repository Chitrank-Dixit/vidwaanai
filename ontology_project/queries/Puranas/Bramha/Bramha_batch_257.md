# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Bramha 0.5121)
- **Original**: (165 । 15-16)
- **Translation**: 

---

### Verse 2 (Bramha 0.5122)
- **Original**: « भद्रतीर्थ, पतत्रितीर्थ और विप्रतीर्थकी महिमा « 249 बहुतेरे दुःखीं भी दिखायी दिये। हर्षणने सनातन
- **Translation**: 

---

### Verse 3 (Bramha 0.5123)
- **Original**: यदि प्रसन्न हो जायें तो तुम्हारे समस्त मनोरथोंकों धर्मस्वरूप अपने मामाको प्रणाम करके पूछा--' तात !
- **Translation**: 

---

### Verse 4 (Bramha 0.5124)
- **Original**: पूर्ण कर देंगे।' ये कौन सुखी हैं और कौन नरकमें कष्ट भोगते हैं?! यह सुनकर हर्षण गौतमी-तटपर गया और उसके इस प्रकार पूछनेपर धर्मराजने सब बातें
- **Translation**: 

---

### Verse 5 (Bramha 0.5125)
- **Original**: स्तरान आदिसे पवित्र हो देवेश्वर भगवान्‌ विष्णुकी ठौक-टठोक बता दीं। उन्होंने कर्मोंकी सम्पूर्ण स्तुति करने लगा। इससे प्रसन्न होकर श्रीहरिने शर्तियोंका पूर्णरूपसे निरूपण किया। वे बोले--'जो
- **Translation**: 

---

### Verse 6 (Bramha 0.5126)
- **Original**: हर्षणको वरदान दिया-- तुम्हारे कुलका कल्याण मनुष्य विहित कर्मका कभी उल्लह्नन नहीं करते,
- **Translation**: 

---

### Verse 7 (Bramha 0.5127)
- **Original**: हो। समस्त अभद्रों (अमड्भलों)-की शान्ति होकर उन्हें नरक नहीं देखना पड़ता। जो शास्त्र और
- **Translation**: 

---

### Verse 8 (Bramha 0.5128)
- **Original**: भद्र (मज्जल)-का विस्तार हो।' “भद्गम्‌ अस्तु' शास्त्रीय सदाचारको नहीं मानते, बहुश्रुत विद्वानोंका
- **Translation**: 

---

### Verse 9 (Bramha 0.5129)
- **Original**: कहनेसे हर्षणके पिता भद्र कहलाये और माता आदर नहीं करते और विहित कर्मोका उल्लड्घन
- **Translation**: 

---

### Verse 10 (Bramha 0.5130)
- **Original**: विष्टिका नाम भद्रा हुआ। तबसे वह स्थान करते हैं, थे मनुष्य नरकगामी होते हैं।'* धर्मतजका
- **Translation**: 

---

### Verse 11 (Bramha 0.5131)
- **Original**: भद्गतीर्थके नामसे प्रसिद्ध हुआ। बह सब प्रकारसे यह बचन सुनकर हर्षणने पुनः कहा-- सुरश्रेष्ट !
- **Translation**: 

---

### Verse 12 (Bramha 0.5132)
- **Original**: मकुलदायक तथा तीर्थसेवी पुरुषोंको सब प्रकारकी मेरे पिता विश्वरूप बड़े भयंकर हैं। मेरी माता
- **Translation**: 

---

### Verse 13 (Bramha 0.5133)
- **Original**: सिद्धि देनेवाला है। वहाँ भद्रपतिके नामसे प्रसिद्ध विष्टि भी भयानक ही हैं। मेरे महाबली भ्राता भी
- **Translation**: 

---

### Verse 14 (Bramha 0.5134)
- **Original**: होकर साक्षात्‌ देवाधिदेव भगवान्‌ जनार्दन श्रीहरि बैसे ही है। जिस उपायसे उन लोगोंकी बुद्धि
- **Translation**: 

---

### Verse 15 (Bramha 0.5135)
- **Original**: निवास करते हैं, जो मड्भलके एकमात्र भण्डार हैं। शान्त हो, वे सुरूप, निर्दोष और मज़्लदायक हो
- **Translation**: 

---

### Verse 16 (Bramha 0.5136)
- **Original**: पतत्रितीर्थ रोगों तथा पापोंका नाश करनेबाला जायें, वह मुझे बताइये। मैं उसे करूँगा, अन्यथा
- **Translation**: 

---

### Verse 17 (Bramha 0.5137)
- **Original**: है। उसके स्मरणमात्रसे मनुष्य कृतकृत्य हो जाता मैं उनके पास लौटकर नहीं जाऊँगा।' हर्षणके यों
- **Translation**: 

---

### Verse 18 (Bramha 0.5138)
- **Original**: है। कश्यपके दो पुत्र हुए-- अरुण और गरुड़। कहनेपर धर्मराजने उस शुद्ध बुद्धिवाले बालकसे
- **Translation**: 

---

### Verse 19 (Bramha 0.5139)
- **Original**: उनके कुलमें पक्षियोंमें श्रेष्ठ सम्पाति उत्पन्न हुए। कहा--'हर्षण ! तुम वास्तवमें हर्षण ही हो। पुत्र
- **Translation**: 

---

### Verse 20 (Bramha 0.5140)
- **Original**: सम्पातिके छोटे भाईका नाम जटायु था। वे दोनों तो बहुत-से होते हैं, किंतु ले सभी कुलका
- **Translation**: 

---

