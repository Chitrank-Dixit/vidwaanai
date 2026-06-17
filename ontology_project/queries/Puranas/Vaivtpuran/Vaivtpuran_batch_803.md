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

### Verse 1 (Vaivtpuran 543.14374)
- **Original**: उन्हें तुम प्राप्त नहीं कर सकी हो। इसीलिये पुत्रशोकसे अपने शरीरको त्याग दिया। श्रीरामचन्रजी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14375)
- **Original**: यह दुष्कर तपस्या कर रही हो। इसी तरह पिताके सत्यको रक्षाके लिये वन-वनमें भ्रमण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14376)
- **Original**: जितेन्द्रियोंमें श्रेष्ठ धर्मात्मा लक्ष्मणको भी प्राप्त करने लगे। कालान्तरमें उस विशाल एवं घोर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14377)
- **Original**: करनेमें तुम्हें सफलता नहीं मिली है; अतः बनमें घूमती हुई रावणकी बहिन शूर्पणखा उधर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14378)
- **Original**: उधरसे निराश होकर तुम तपस्यामें लगी हो। आ निकली। उसने बड़े कौतूृहलसे श्रीरामको तुम्हारी इस तपस्याका फल तुम्हें दूसरे जन्ममें देखा। उन्हें देखते ही वह कुलटा राक्षसी काम-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14379)
- **Original**: मिलेगा। जो ब्रह्मा, विष्णु और शिव आदिके बेदनासे पीड़ित हो गयी। उसके सारे अड्जरॉमें भी ईश्वर तथा प्रकृतिसे भी परे हैं, उन भगवान्‌ रोमाझ हो आया और वह मूच्छित हो गयी। श्रीकृष्णकों तुम पतिरूपमें प्राप्त करोगी। समन वह श्रीरामके पास गयी। शूर्पणखा सदा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14380)
- **Original**: ऐसा कहकर ब्रह्माजी सानन्द अपने बने रहनेवाले यौवनसे युक्त, अत्यन्त प्रौढ़ और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14381)
- **Original**: धामको चले गये और शूर्पणखाने अपने कामोन्मत्त थी। वह मनमें कामभाव ले श्रीरामसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14382)
- **Original**: शरीरको अग्निमें विसर्जित कर दिया। वही दूसरे मुस्कराती हुई बोली। जन्ममें कुब्जा हुई। शूर्पणखाके उकसानेसे शूर्पणखाने कहा--हे राम! हे घनश्याम !
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14383)
- **Original**: मायावी राक्षसराज रावण क्रोधसे काँपने लगा। है रूपधाम! हे गुणसागर! मेरा हृदय आपमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14384)
- **Original**: उसने मायाद्वारा सौताकों हर लिया। सीताकों अनुरक्त हो गया है। आप एकान्त स्थानमें मुझे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14385)
- **Original**: आश्रममें न देख श्रीराम मूच्छित हो गये। तब स्वीकार कौजिये। उनके भाई लक्ष्मणने आध्यात्मिक ज्ञानकी चर्चा तदनन्तर श्रीराम तथा लक्ष्मणसे शूर्पणखाकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14386)
- **Original**: करके उन्हें सचेत किया। मुने! तत्पश्चात्‌ वे * न हि सत्यात्‌ परो धर्मों नानृतातू पातकं परमू ।न हि गज्जासमं तौथ॑ न देव: केशवात्‌ पर:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14387)
- **Original**: नास्ति धर्मात्‌ परो अन्धुर्नास्ति धर्मात्‌ परं धनम्‌ । धर्मात्‌ प्रियः पर: को वा स्वधर्म॑ रक्ष यत्रत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14388)
- **Original**: स्वधर्मे रक्षिते तात शश्वत्‌ सर्वत्र मद्लम्‌ । यशस्यं सुप्रतिष्ठा च प्रताप: पूजन परम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14389)
- **Original**: 21-23)
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14390)
- **Original**: + श्रीकृष्णजन्मखण्ड * 623 &#$6#$ 4 % 445 44 $ $ 5 $ 5 % $ 4 $ $ $ 5 5 5 $ 5 5 # $$ 55 $ 5 % 5 $ 5 $ # 5 # # # # # # $ $ $# # $ # & # # # 46 ### # 4 ##% # # #_ जानकौकी खोजके लिये दिन-रात शोकार्त हो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14391)
- **Original**: समस्त भुवनोंकों पवित्र करनेकी क्षमता थी। गहन वन, पर्वत, कन्दरा, नद, नदी और मुनियोंके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14392)
- **Original**: उस समय रोती हुई माता जानकीकों देखकर आश्रमोंमें घूमने लगे। सुदीर्ध कालतक अन्वेषण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14393)
- **Original**: पवननन्दन हनुमान्‌ने प्रसन्नतापूर्वक उनके हाथमें करनेपर भी जब उन्हें जानकौका पता न चला,
- **Translation**: 

---

