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

### Verse 1 (Vaivtpuran 543.15034)
- **Original**: उस ज्ञानकी चर्चा की। नारद! ब्रह महाज्ञान पाकर कठोर कर्मोमें तप, फलोंमें मोक्ष, अष्ट सिद्धियोंमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15035)
- **Original**: सब लोगोंने अपना शोक त्याग दिया। श्रीकृष्ण प्राकाम्य, पुरियोंमें काशी, नगरोंमें काझछी, देशोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15036)
- **Original**: यद्यपि निर्लिप्त हैं, तथापि मायाके स्वामी हैं; बैष्णवोंका देश और समस्त स्थूल आधारोंमें मैं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15037)
- **Original**: इसलिये मायासे अनुरक्त जान पड़ते हैं। यशोदाजीने ही महान्‌ विराट हूँ। जगत्‌में जो अत्यन्त सूक्ष्म
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15038)
- **Original**: पुनः नन्दरायजीकों माधवके पास भेजा। उनकी पदार्थ हैं; उनमें मैं परमाणु हूँ। बैद्योंमें अश्विनीकुमार,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15039)
- **Original**: प्रेरणासे फिर आकर नन्‍्दजीने त्रह्माजीके द्वारा किये भेषजोंमें रसायन, मन्त्रवेत्ताओँमें धन्वन्तरि, विनाशकारी गये सामवेदोक्त स्तोत्रसे परमानन्दस्वरूप नन्‍्दनन्दन दुर्गुणोंमें बिषाद, रागोंमें मेघ-मलार, रागिनियोंमें माधवकी स्तुति की । तत्पश्चात्‌ वे पुत्रके सामने खड़े कामोद, मेरे पार्षदोंमें श्रीदामा, मेरे बन्धुओंमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15040)
- **Original**: हो बार-बार रोदन करने लगे। (अध्याय 73) #++2+“>अ्यस्येट >> ल>
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15041)
- **Original**: # श्रीकृष्णजन्मखण्ड + 653 श्रीकृष्णद्वारा नन्दजीको ज्ञानोपदेश, लोकनीति, लोकमर्यादा तथा लौकिक सदाचारसे सम्बन्ध रखनेवाले विविध विधि-निषेधोंका वर्णन, कुसड्र और कुलटाकी निन्दा, सती और भक्तकी प्रशंसा, शिवलिड्ड-पूजन एवं शिवकी महत्ता श्रीनारायण कहते हैं--नारद! भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15042)
- **Original**: ज्ञान प्रदान किया। श्रीकृष्ण परमानन्दमय परिपूर्णतम प्रभु हैं। भक्तोपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15043)
- **Original**: . भ्रीभगवान्‌ बोले--तात ! मैं तुम्हें वह परम अनुग्रहके लिये व्याकुल रहनेवाले परम परमात्मा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15044)
- **Original**: अद्भुत ज्ञान प्रदान करता हूँ, जो वेदोंमें अत्यन्त हैं। पृथ्वोका भार उतारनेके लिये अबतोर्ण हुए
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15045)
- **Original**: गोपनीय और पुराणोंमें अत्यन्त दुर्लभ है, कुलय वे भगवान्‌ निर्गुण, प्रकृतिसे परे तथा परात्पर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15046)
- **Original**: स्त्रियाँ मोक्ष-मार्गके ट्वारको ढकनेके लिये अर्गलाएँ हैं। ब्रह्मा, शिव और शेष भी उनके चरणोंको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15047)
- **Original**: हैं, भ्रम और मायाको सुन्दर भूमियाँ हैं; उनपर बन्दना करते हैं। नन्‍्दजीकी स्तुति सुनकर वे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15048)
- **Original**: कभी विश्वास नहीं करना चाहिये। ब्रजराज! जगदीश्वर बहुत संतुष्ट हुए। नन्‍द बाबा विरहज्वरसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15049)
- **Original**: असाध्वी स्त्रियाँ हरिभक्तिके विरुद्ध होती हैं। वे कातर हो गोकुलसे उनके पास आये थे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15050)
- **Original**: नाशकों बीजरूपा हैं। उनपर विश्वास करना श्रीभगवानने उनसे इस प्रकार कहा-- बाबा!
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15051)
- **Original**: कदापि उचित नहीं है। प्रतिदिन प्रातःकाल उठकर शोक और भ्रमको छोड़ो तथा ब्रजको लौट जाओ।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15052)
- **Original**: रातमें पहने हुए कपड़ोंकों त्याग दे और हृदय- वहाँ जाकर सबको आनन्दित करो। मैं जो परम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15053)
- **Original**: कमलमें इशष्टदेवका तथा ब्रह्मरन्श्रमें परम गुरुका सत्य ज्ञान बता रहा हूँ, इसे सुनो। यह ज्ञान
- **Translation**: 

---

