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

### Verse 1 (Vishnu Puran 0.4241)
- **Original**: 69 ब्राह्मण उवायच नाह॑ पीवान्न चैवोढा शिबिका भवतो मया । न श्रान्तोस्मि न चायासो सोठव्यो5स्ति महीपते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4242)
- **Original**: 62 राजोकाच प्रत्यक्ष दृश्यसे पीवानद्यापि शित्रिका त्वग्रि । श्रमअश्॒भारोइहने भवत्येव हि देहिनाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4243)
- **Original**: 63 ब्राह्मण उवाच प्रत्यक्ष भवता भूप यददु्ट मम तद्ठद। बलवानबलश्षेति वाच्य पश्चाद्रिशेषणम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4244)
- **Original**: 64 त्वयोढा शिब्िका चेति त्वव्यद्यापि च संस्थिता । मिथ्यैतदत्र॒ तु भवाज्छुणोतु बचने, मम
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4245)
- **Original**: 65 भूमौ पादयुर्ग त्वास्ते जल्डे पादद्रये स्थिते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4246)
- **Original**: ऊवॉर्जड्डाद्ययावस्थी तदाधारं तथोदरम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4247)
- **Original**: 66 बक्ष:स्थलं तथा बाहू स्कन्‍्धौ चोदरसंस्थितौ । स्कशथचश्नितेय॑ शिब्िका मम भारो5म्र कि कृत:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4248)
- **Original**: 67 शिबिकायां स्थित चेद॑ वपुस्त्वदुपलक्षितम्‌ । तत्र त्वमहमप्थत्र प्रोच्यते चेदमन्यथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4249)
- **Original**: 68 अहं त्व॑ च तथान्ये च भूतैरुद्माम पार्थिव । गुणप्रवाहपतितो भूतबर्गोडपि य्रात्ययम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4250)
- **Original**: 69 कर्मवहश्या गुणाश्षैते सत्त्वाद्या: पृथिबीपते । अविद्यासञितं कर्म तथ्चाशेषेषु जन्तुषु
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4251)
- **Original**: 70 आत्पा शुद्धो5क्षरः शान्तो निर्गुण: ग्रकृतेः पर: । प्रबृद्धयपत्नयौँ नास्य एकस्याखिल्लजन्तुषु
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4252)
- **Original**: 71 द्वितीय अंज्ञ 151 जल्दी चल रहे थे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4253)
- **Original**: इस प्रकार शिबिक्य्रकी बरिषम-गति देखकर राजाने कहा---''अरे दिविकाबाहकों ! यह क्‍या करते हो ? समान गतिसे चल्म्रे''
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4254)
- **Original**: किन्तु फिर भी उसकी गति उसी प्रकार विषम देखकर राजाने फिर कहा--“' अरे क्या है ? इस प्रकार असमान भावसे क्‍यों चलते हो ? '
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4255)
- **Original**: राजाके बार-बार ऐसे वचन सुनकर ते शिविकावाहक [भग्तजीको दिखाकर] कहने लो-- “हममेंसे एक यही धरे-धीरे चलता है”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4256)
- **Original**: राजाने कहा-- अरे, तुने तो अभी मेरी शिक्षिकाको थोड़ी ही दूर बहन किया है; क्या इतनेहीमें थक गया ? तू जैसे तो बहुत मोटा-मुष्टण्डा दिखायी देता है, फिर क्‍या तुझसे इतना भी श्रम नहीं सहा जाता ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4257)
- **Original**: ब्राह्मण बोले--राजन्‌ ! मैं न मोटा हूँ और - मैंने आपकी शिबिका ही उठा रखो है। मैं थका भी नहीं हूँ और न मुझे श्रम सहन करनेकी ही आवश्यकता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4258)
- **Original**: राजा बोलछे--ओरे, तू तो प्रत्यक्ष ही मोटा दिखायी दे रहा है, इस समय भी शिबिका तेरे कन्धेपर रखी हुई है और बोझा ढोनेसे देहभारियोंको श्रम होता ही है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4259)
- **Original**: ब्राह्मण बोलले--राजन्‌ ! तुम्हें प्रत्यक्ष क्या दिखायी दे रहा है, मुझे पहले यही बताओ। उसके 'बलवान्‌ अथवा “अबलवान्‌' आदि बिशेषणोंकी बात तो पीछे करना
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4260)
- **Original**: “तूने मेरी दिव्ििकाका वहन किया है, इस समय भी ञह तेरे हो कन्धोंपर रखी हुई है'--- तुम्हारा ऐसा कहना सर्वथा मिध्या है, अच्छा मेरी बात सूनो--
- **Translation**: 

---

