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

### Verse 1 (Vaivtpuran 16.3654)
- **Original**: प्रास करके वह गोलोकमें चला गया। अब मैं तुम्हारी तपस्थाका फल देना उचित समझता हूँ। जबकि तुम इस शरीरका त्याग करके दिव्य देह अपने सामने उन सनातन प्रभु देवेश्वर श्रीहरिको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3655)
- **Original**: धारणकर मेरे साथ आनन्द करो। लक्ष्मीके समान विराजमान देखा। भगवान्‌का दिव्य विग्रह नूतन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3656)
- **Original**: तुम्हें सदा मेरे साथ रहना चाहिये। तुम्हारा यह मेघके समान श्याम था। आँखें शरत्कालीन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3657)
- **Original**: शरीर नदीरूपमें परिणत हो “गण्डकौ' नामसे कमलकी तुलना कर रही थीं। उनके अलौकिक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3658)
- **Original**: प्रसिद्ध होगा। यह पवित्र नदी पुण्यमय भारतवर्षमें रूप-सौन्दर्यमें करोड़ों कामदेवोंकी लावण्य-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3659)
- **Original**: मनुष्योंकों उत्तम पुण्य देनेवाली बनेगी। तुम्हारे लीला प्रकाशित हो रही थी। रत्रमय भूषण उन्हें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3660)
- **Original**: केशकलाप पवित्र वृक्ष होंगे। तुम्हारे केशसे उत्पन्न आभूषित किये हुए थे। उनका प्रसन्नवदन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3661)
- **Original**: होनेके कारण तुलसीके नामसे ही उनकी प्रसिद्धि मुस्कानसे भरा था। उनके दिव्य शरौरपर पीताम्बर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3662)
- **Original**: होगी। वरानने! तीनों लोकॉंमें देवताओंकी पूजाके सुशोभित था। उन्हें देखकर पतिके निधनका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3663)
- **Original**: काममें आनेवाले जितने भी पत्र और पुष्प हैं, उन अनुमान करके कामिनी तुलसी मूच्छित हो गयी।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3664)
- **Original**: सबमें तुलसी प्रधान मानी जायगी। स्वर्गलोक, फिर चेतना प्राप्त होनेपर उसने कहा। मर्त्यलोक, पाताल तथा वैकुण्ठ-लोकपें--सर्वत्र तुलसी बोली--नाथ ! आपका हृदय पाषाणके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3665)
- **Original**: तुम मेरे संनिकट रहोगी। सुन्दरि! तुलसीके वृक्ष सदृश है; इसोलिये आपमें तनिक भी दया नहीं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3666)
- **Original**: सब पुष्पोंमें श्रेष्ठ हों। गोलोक, विरजा नदीके तर, है। आज आपने छलपूर्वक (मेरे इस शरीरका)
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3667)
- **Original**: रासमण्डल, वृन्दावन, भूलोक, भाण्डीरवन, धर्म नष्ट करके मेरे (इस शरीरके) स्वामौकों
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3668)
- **Original**: चम्पकवन, मनोहर चन्दनवन एबं माधवी, केतकी,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3669)
- **Original**: श्ध्ढ़ + संक्षिप्त ब्रह्मबैवर्तपुराण « 5355%$$£#$$ 5 4 $ 45 6 $ 5 5 $ 1 $ %$ £# 55 $ 54 5 5 $ $ 45 £ 5 5 $ 5 £5 55 6 5 4 4 # $% # 44 ; # 44 $ 4 644 48 688 88 68 5 5 5 5 % कुन्द और मल्लिकाके बनमें तथा सभी पुण्य
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3670)
- **Original**: चला जाता है। तुलसी-काष्ठकी मालाको गलेमें स्थानोमें तुम्हारे पुण्यप्रद वृक्ष उत्पन्न हों और रहें।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3671)
- **Original**: धारण्‌ क्लरनेवाला पुरुष पद-पदपर अश्रमेध- तुलसी-वृक्षेक नीचेके स्थान परम पवित्र एवं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3672)
- **Original**: यज्ञके फलका भागी होता है, इसमें संदेह नहीं। पुण्यदायक होंगे; अतएब बहाँ सम्पूर्ण तीथों और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3673)
- **Original**: . जो मनुष्य तुलसीको अपने हाथपर रखकर समस्त देवताओंका भी अधिष्ठान होगा। वरानने !
- **Translation**: 

---

