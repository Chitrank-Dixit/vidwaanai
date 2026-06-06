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

### Verse 1 (Vaivtpuran 15.6653)
- **Original**: है; अत: चलो, मैं तुम्हारे साथ चलता हूँ। वहाँ कृत्तिकाएँ प्रकृतिकी कलाएँ हैं। इन्होंने निरन्तर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6654)
- **Original**: देवसमुदायका दर्शन करूँगा। (अध्याय 14-15) +++->+-अय्यंश्य तल कार्तिकेयका नन्दिके श्वरके साथ कैलासपर आगमन, स्वागत, सभामें जाकर विष्णु आदि देवोंको नमस्कार करना और शुभाशीर्वांद पाना श्रीनारायणजी कहते हैं--नारद ! शंकरसुवन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6655)
- **Original**: बन्धुवर्ग तथा माताको देखना चाहता हूँ; अतः कार्तिकेय नन्दिकेश्वसे यों कहकर शीघ्र ही
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6656)
- **Original**: शंकरजीके निवासस्थानपर जाऊँगा, इसके लिये कृत्तिकाओंको समझाते हुए नीतियुक्त वचन बोले।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6657)
- **Original**: आपलोग मुझे आज्ञा प्रदान करें। सारा जगतू, कार्तिकेयने कहा--माताओ ! मैं देवसमुदाय,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6658)
- **Original**: शुभदायक जन्म-कर्म, संयोग-वियोग सभी दैवके + स्तनदात्री गर्भधात्री भक्ष्यदात्री गुरुप्रिया । अभीष्टदेवपत्नी च पितुः पत्नी च कन्यका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6659)
- **Original**: सगर्भकन्याभगिनी पुत्रपत्री प्रियाप्रसू: । मातुर्माता पितुर्माता सोदरस्य प्रिया तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6660)
- **Original**: मातु: पितुश्ध भगिनी मातुलानी तथैव च। जनानां वेदबिहिता मातरः षोडश स्मृता:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6661)
- **Original**: (गणपतिखण्ड 15। 38--40 )
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6662)
- **Original**: 328 ] संक्षिप्त ग्रह्मवैवर्तपुराण न्‍] %#%#% 65% 5 $ % % ऋ4## # 8 #
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6663)
- **Original**: 8 5 ऊऊ#%4#/ 68% 8 5 8 5 5 45 5 5888 48 85 5 55 5 45 9588 86685 56244 64 अधीन है। दैवसे बढ़कर दूसरा कोई बली नहीं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6664)
- **Original**: उसकी अपूर्व शोभा हो रही थी। पारिजात- है। वह दैव श्रीकृष्णके वशमें रहनेवाला है;
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6665)
- **Original**: पुष्पोंकी मालावलीसे वह सुशोभित था। मणियोंके क्योंकि वे दैवसे परे हैं। इसीलिये संतलोग उन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6666)
- **Original**: दर्पण तथा श्वेत चँंवरॉंसे वह अत्यन्त उद्धासित ऐश्वर्यशाली परमात्माका निरन्तर भजन करते हैं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6667)
- **Original**: हो रहा था और चित्रकारीयुक्त रमणीय क्रौडा- अविनाशी श्रीकृष्ण अपनी लीलासे दैवको बढ़ाने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6668)
- **Original**: भवनोंसे वह भलीभाँति सुसज्जित था। वह मनोहर और घटानेमें समर्थ हैं। उनका भक्त दैवके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6669)
- **Original**: तो था ही, उसका विस्तार भी बड़ा था। उसमें वशीभूत नहीं होता-ऐसा निर्णीत है। इसलिये
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6670)
- **Original**: सौ पहिये लगे थे। उसका वेग मनके समान था आपलोग इस दुःखदायक मोहका परित्याग
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6671)
- **Original**: और श्रेष्ठ पार्षद उसे घेरे हुए थे। उस रथको कीजिये और जो सुखदाता, मोक्षप्रद, सारसर्वस्व,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6672)
- **Original**: पार्वतीने भेजा था। उस रथपर कार्तिकेयको चढ़ते जन्म-पृत्युके भयके बिनाशकर्ता, परमानन्दके
- **Translation**: 

---

