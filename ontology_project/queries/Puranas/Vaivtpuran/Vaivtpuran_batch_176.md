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

### Verse 1 (Vaivtpuran 12.10006)
- **Original**: ही होता है। समस्त गोपरूपी कमलवनोंके आप मेरे इस दोषको क्षमा कर देंगे। साधुपुरुष विकासके लिये गोपराज गिरिभानु सूर्यके समान सदा हो मूढ़ मनुष्योंके दोषोंकों क्षमा करते हैं। उनकी पत्नीका नाम सती पद्मावती है, जो रहते हैं।' साक्षात्‌ पद्मा (लक्ष्मी)-के समान हैं। उन्हींको तदनन्तर अड्भिरा, अत्रि, मरीचि और गौतम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.10007)
- **Original**: कन्या तुम यशोदा हो, जो अपने यशकी वृद्धि आदि बहुत-से ऋषि-मुनियोंके नाम लेकर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.10008)
- **Original**: करनेवाली हो। भद्रे! नन्द और तुम जो कुछ यशोदाने पूछा--' प्रभो! इन पुण्यश्लोक महात्माओंमेंसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.10009)
- **Original**: भी हो, वह मुझे ज्ञात है। यह बालक जिस आप कौन हैं। कृपया मुझे बताइये
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.10010)
- **Original**: यद्यपि आपसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.10011)
- **Original**: प्रयोजनसे भूतलपर अवतीर्ण हुआ है, वह सब उत्तर पानेके योग्य मैं नहीं हूँ, तथापि आप मुझे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.10012)
- **Original**: मैं जानता हूँ। निर्जन स्थानमें नन्‍्दके समीप मैं मेरी पूछी हुई बात बताइये। आप-जैसे महात्मा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.10013)
- **Original**: सब बातें बताऊँगा। मेरा नाम गर्ग है। मैं
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.10014)
- **Original**: 450 * संक्षिप्त ख्रह्म॑वैवर्तपुराण « 4$$%#%#4% 44 $$ ## # ## 44 ## # # 6 # 646 $# 4449 8659 ##% ## #/ # 5 5 5 ## 5 55 $ 5 55 55 45 15 $ $ 54 8 5 8 6 8 चिरकालसे यदुकुलका पुरोहित हूँ। वसुदेवजीने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.10015)
- **Original**: वह तेजोराशि ही मूर्तिमान्‌ होकर उनके यहाँ मुझे यहाँ ऐसे कार्यके लिये भेजा है, जिसे दूसरा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.10016)
- **Original**: अवतीर्ण हुई है। भगवान्‌ श्रीकृष्ण बसुदेवको कोई नहीं कर सकता। अपना रूप दिखाकर शिशुरूप हो गये और इसी बीचमें गर्गनीका आगमन सुनते ही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.10017)
- **Original**: सूतिकागारसे इस समय तुम्हारे घरमें आ गये नन्‍्दजी वहाँ आ पहुँचे। उन्होंने दण्डकी भाँति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.10018)
- **Original**: हैं।ये किसी योनिसे प्रकट नहीं हुए हैं; अयोनिज पृथ्वीपर माथा टेक उन मुनीश्वरकों प्रणाम किया।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.10019)
- **Original**: रूपमें ही भूतलपर प्रकट हुए हैं। इन श्रीहरिने साथ ही उनके शिष्योंकों भी मस्तक झुकाया।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.10020)
- **Original**: मायासे अपनी माताके गर्भको वायुसे पूर्ण कर उन सबने उन्हें आशीर्वाद दिये। इसके बाद रखा था। फिर स्वयं प्रकट हो अपने उस दिव्य गर्गजी आसनसे उठे और नन्‍्द-यशोदाकों साथ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.10021)
- **Original**: रूपका वसुदेवजीको दर्शन कराया और फिर ले सुरम्य अन्तःपुरमें गये। उस निर्जन स्थानमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.10022)
- **Original**: शिशुरूप हो वे यहाँ आ गये। गर्ग, नन्द और पुत्रसहित यशोदा इतने ही लोग। ._गोपराज! युग-युगमें इनका भिन्न-भिन्न वर्ण रह गये थे। उस समय गर्गजीने यह गूढ़
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.10023)
- **Original**: और नाम है; ये पहले श्वेत, रक्त और पीतवर्णके बात कही। थे। इस समय कृष्णवर्ण होकर प्रकट हुए हैं। श्रीगर्गजी बोले--नन्द! मैं तुम्हें मड्न्‍गलकारी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.10024)
- **Original**: सत्ययुगमें इनका वर्ण श्वेत था। ये तेज:पुञसे वचन सुनाता हूँ। बसुदेवजीने जिस प्रयोजनसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.10025)
- **Original**: आवृत होनेके कारण अत्यन्त प्रसन्न जान पड़ते मुझे यहाँ भेजा है, उसे सुनो। बसुदेवने
- **Translation**: 

---

