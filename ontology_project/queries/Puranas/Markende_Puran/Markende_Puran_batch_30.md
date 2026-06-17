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

### Verse 1 (Markende Puran 0.581)
- **Original**: यादाततपांसोड परत च न भूतप्रे , भवन्ति तस्य वस्थर्तपरिक्राण न सातसप्‌। नरस्य यय्पय कहिएयं सगो बाक्षतुरादिएु
- **Translation**: 

---

### Verse 2 (Markende Puran 0.582)
- **Original**: बृद्धेषू चनह्ंनन्ये मानुपँ रक्षझों हि सः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.583)
- **Original**: एतेषा संतिकर्षात्‌ तु घद्॒ग्सिपरितापज़म्‌ ! तधेग़गस्थ्वज॑जापि दुःछझे तरकसमस्धवभता श्षत्पपास्ताभर्व दुशरत्न यज्य मूच्छीप्रद॑ महते । एोषों त्राणद/नं लु मन्‍्ये स्जर्गसुखात्‌ परए
- **Translation**: 

---

### Verse 4 (Markende Puran 0.584)
- **Original**: प्राप्स्यन्त्यवार्ता यदि गुर्ख बदको दुःखणिते गपि । कि; प्रा मया + स्यात तष्यात त्वं उ0 या चिएमआ (आअ0 15! 56--65)
- **Translation**: 

---

### Verse 5 (Markende Puran 0.585)
- **Original**: 50 * संक्षिम मार्कण्डेय पुराण * 68574 .&2/8% # 42:26 #्862:7464 ढ5:2%7 4 6:307%652247& 464 / 5283 82/#4770 66:25 5677 66:54 8327 66084 32 अभिलाषा क्यों करेंगे? अतः मेरा जो कुछ भी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.586)
- **Original**: ऋज्ड्स पुष्य है, उसके द्वारा थे यातनामें पड़े हुए पायो
- **Translation**: 

---

### Verse 7 (Markende Puran 0.587)
- **Original**: >#धट जीव नरकसे छुटकारा पा जाये। ये पापी जीव भी नरकसे मुक्त हो गये। पुत्र कहता है-- पिताजी ! तटनन्तर गज विपक्ित्के
- **Translation**: 

---

### Verse 8 (Markende Puran 0.588)
- **Original**: ऊपर फूलोंओी बर्षा होने लगो और स्श्रयं भगवान्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.589)
- **Original**: किण्णु उन्हें विमादमें वित्यकर दिव्वधाममें ले गये ।* उस समय मैं तथा और भी जितने पापी जीव थे,
- **Translation**: 

---

### Verse 10 (Markende Puran 0.590)
- **Original**: बे सब नरकयातनासे छूटकर अपने-अपने कर्मफलके अनुसार भिन्न भिन्न योतियोंपं चले गये। द्विजश्रेष्ठ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.591)
- **Original**: इस प्रकार मैंदे $न नरक्ोंक। बर्णन किया; साथ हो
- **Translation**: 

---

### Verse 12 (Markende Puran 0.592)
- **Original**: पूव॑कालमें मैंने जैसा अनुभव किया था, उसके अनुसार जिस-जिस पापके कारण मनुष्य जिस-
- **Translation**: 

---

### Verse 13 (Markende Puran 0.593)
- **Original**: 15) जिस नोनिमें जाता है, कह सब भी बतला दिया।। «35 _ज>-चिकरपदा22>>> द्त्तात्रेयजीके जन्म-प्रसड्भमें एक पतिक्रता ब्राह्मणी तथा अनसूयाजीका चरित्र पिता बोले-- बेटा! तुमने अत्यन्त हेय रंसारके ' मुझे क्या करना चाहिये? यह बताओं। व्यवस्थित स्वकृपका हर्णन किया, जो घहों-
- **Translation**: 

---

### Verse 14 (Markende Puran 0.594)
- **Original**: पुत्र ( सुमति ) ने कहां--पिताजी! यदि आप यनल्रकों भाँति गिस्तर आव्यगमनशील और ग्रवाहरूपते , शझ्टा छोड़कर मेरे बचमॉँमें पूर्ण श्रद्धा रखते हैं अविनाशी है। इस प्रकार पैने इसके स्थ्रूपकों
- **Translation**: 

---

### Verse 15 (Markende Puran 0.595)
- **Original**: तो मेरी राज यह हैं कि आप पृहस्थाश्रमका लीभाँजत समझ लिया है। ऐसी स्थितिमें अब
- **Translation**: 

---

### Verse 16 (Markende Puran 0.596)
- **Original**: परित्याग करके लत्रानप्रस्थके नियमोंका पालत सापुद्त उताकच-छा अमंश्ध शक्रश ह्थं जेतुं रामुपागतों । अकल्वास्यड्नन्तत्यें कमात्‌ पर्थिय गम्काय्‌
- **Translation**: 

---

### Verse 17 (Markende Puran 0.597)
- **Original**: भ्र्थ जणव-नयामि त्वापह ज्ठर्ग त्तथा सम्सगुणासतः
- **Translation**: 

---

### Verse 18 (Markende Puran 0.598)
- **Original**: विपाननेतदारुद्म सा णिशावस्य गम्यलामू
- **Translation**: 

---

### Verse 19 (Markende Puran 0.599)
- **Original**: गजोछात्र -“गरके मात थर्स भोड्य्लैउत सहरश्त: : जाहोति आर्ता: ऋत्दत्ति परत़ो न च्जाप्यहसू
- **Translation**: 

---

### Verse 20 (Markende Puran 0.600)
- **Original**: यदि जाताएि धर्म त्वं त्य॑ वा शक्र॒ शाचीण्ते
- **Translation**: 

---

