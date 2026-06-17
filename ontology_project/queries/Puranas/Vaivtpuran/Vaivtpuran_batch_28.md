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

### Verse 1 (Vaivtpuran 4.8456)
- **Original**: (गणपतिखण्ड 4ड4ड। 85-98)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8457)
- **Original**: * गणपत्तिखण्ड « 393 45564 ####£## 44544 4 484 85644 4 # 64448 # 4 # 54% 44444 44 4444 ### 4 # 8 #/ 85 46686 # 8 ###अऋ 4 नारद! यों कहकर भगवान्‌ विष्णु शीघ्र ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8458)
- **Original**: नि:श्वास प्रकट हुआ। वह नि: श्वास महावायु हुआ वैकुण्ठको चले गये। श्रीहरिके चले जानेपर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8459)
- **Original**: और वही विश्वको धारण करनेवाला विराट परशुराम हरिका स्मरण करके विष्णुप्रदत्त स्तोत्रद्वारा, कहलाया। तुम्हारे पसीनेसे विश्वगोलक पिघल जो सम्पूर्ण विप्नोंका नाशक तथा धर्म-अर्थ-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8460)
- **Original**: गया। तब विश्वका निवासस्थान वह विराट्‌ काम-मोक्षका कारण है; उन दुर्गाकी स्तुति
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8461)
- **Original**: जलकी राशि हो गया। तब तुमने अपनेकों पाँच करनेको उद्यत हुए। उन्होंने गद्गाके शुभजलमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8462)
- **Original**: भागोंमें विभक्त करके पाँच मूर्ति धारण कर ली। स्नान करके धुले हुए वस्त्र धारण किये। फिर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8463)
- **Original**: उनमें परमात्मा श्रीकृष्णकी जो प्राणाधिष्ठात्री मूर्ति अअञ्जलि बाँधकर भक्तेश्वर गुरुको प्रणाम किया।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8464)
- **Original**: है, उसे भविष्यवेत्ता लोग कृष्णप्राणाधिका “राधा' फिर आचमन करके दुर्गकों सिर झुकाकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8465)
- **Original**: कहते हैं। जो मूर्ति वेद-शास्त्रोंकी जननी तथा नमस्कार किया। उस समय भक्तिके कारण उनके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8466)
- **Original**: वेदाधिष्ठात्री है, उस शुद्धरूपा मूर्तिकों मनीषीगण कंधे झुके हुए थे, आँखोंमें आनन्दाश्रु छलक आये
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8467)
- **Original**: 'सावित्री' नामसे पुकारते हैं। जो शान्ति तथा थे और सारा अद्भ पुलकायमान हो गया था। शान्तरूपिणी ऐश्वर्यकी अधिष्ठात्री मूर्ति है, उस परशुरामने कहा--प्राचीन कालकी बात
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8468)
- **Original**: सत्त्वस्वरूपिणी शुद्ध मूर्तिको संतलोग “लक्ष्मी' है; गोलोकमें जब परिपूर्णतम श्रीकृष्ण सृष्टि-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8469)
- **Original**: नामसे अभिहित करते हैं। अहो! जो रागकी रचनाके लिये उद्यत हुए, उस समय उनके शरीरसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8470)
- **Original**: अधिष्ठात्री देवी तथा सत्पुरुषोंकों पैदा करनेवाली तुम्हारा प्राकट्य हुआ था। तुम्हारी कान्ति करोड़ों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8471)
- **Original**: है, जिसकी मूर्ति शुक्ल वर्णकी है, उस शास्त्रकी सूर्योके समान थी। तुम वस्त्र और अलंकारोंसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8472)
- **Original**: ज्ञाता मूर्तिको शास्त्रज्ञ 'सरस्वती' कहते हैं। जो विभूषित थीं। शरीरपर अग्निमें तपाकर शुद्ध कौ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8473)
- **Original**: मूर्ति बुद्धि, विद्या, समस्त शक्तिकी अधिदेवता, हुई साड़ीका परिधान था। नव तरुण अवस्था
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8474)
- **Original**: सम्पूर्ण मड्गलोंकी मद्जलस्थान, सर्वमज्गलरूपिणी थी। ललाटपर सिंदूरकी बेंदी शोभित हो रही
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8475)
- **Original**: और सम्पूर्ण मड्रलॉंकी कारण है, बही तुम इस थी। मालतीकी मालाओंसे मण्डित गुँथी हुई सुन्दर [समय शिवके भवनमें विराजमान हो। चोटी थी। बड़ा ही मनोहर रूप था। मुखपर
- **Translation**: 

---

