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

### Verse 1 (Vaivtpuran 543.14314)
- **Original**: ब्रह्माजी बोले--वरानने ! श्रीराम दुर्लभ हैं। बनमें चले गये। मुने! इधर महाराज दशरथने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14315)
- **Original**: उन्हें तुम प्राप्त नहीं कर सकी हो। इसीलिये पुत्रशोकसे अपने शरीरको त्याग दिया। श्रीरामचन्रजी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14316)
- **Original**: यह दुष्कर तपस्या कर रही हो। इसी तरह पिताके सत्यकी रक्षाके लिये वन-वनमें भ्रमण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14317)
- **Original**: जितेन्द्रियोंमें श्रेष्ठ धर्मात्मा लक्ष्मणकों भी प्राप्त करने लगे। कालान्तरमें उस विशाल एवं घोर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14318)
- **Original**: करनेमें तुम्हें सफलता नहीं मिली है; अतः बनमें घूमती हुई रावणकी बहिन शूर्पणखा उधर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14319)
- **Original**: उधरसे निराश होकर तुम तपस्यामें लगी हो। आ निकली। उसने बड़े कौतूहलसे श्रीरामको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14320)
- **Original**: तुम्हारी इस तपस्याका फल तुम्हें दूसरे जन्ममें देखा। उन्हें देखते ही वह कुलटा राक्षसी काम-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14321)
- **Original**: मिलेगा। जो ब्रह्मा, विष्णु और शिव आदिके बेदनासे पीड़ित हो गयी। उसके सारे अड्जोंमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14322)
- **Original**: भी ईश्वर तथा प्रकृतिसे भी परे हैं, उन भगवान्‌ रोमाझ्ञ हो आया और वह मूर्च्छित हो गयी।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14323)
- **Original**: श्रीकृष्णको तुम पतिरूपमें प्राप्त करोगी। फिर वह श्रीरामके पास गयी। शूर्पणखा सदा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14324)
- **Original**: । ऐसा कहकर. ब्रह्माजी सानन्द अपने बने रहनेवाले यौवनसे युक्त, अत्यन्त प्रौढ़ और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14325)
- **Original**: धामको चले गये और शूर्पणखाने अपने कामोन्मत्त थी। वह मनमें कामभाव ले श्रीरामसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14326)
- **Original**: शरीरको अग्रनिमें विसर्जित कर दिया। वही दूसरे मुस्कराती हुई बोली। जन्ममें कुब्जा हुई। शूर्पणखाके उकसानेसे शूर्पणखाने कहा--हे राम! हे घनश्याम!
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14327)
- **Original**: मायाबी राक्षसराज रावण क्रोधसे काँपने लगा। हे रूपधाम! हे गुणसागर! मेरा हृदय आपमें उसने मायाद्वारा सीताकों हर लिया। सीताकों अनुरक्त हो गया है। आप एकान्त स्थानमें मुझे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14328)
- **Original**: आश्रममें न देख श्रीराम मूर्च्छित हो गये। तब स्वीकार कीजिये। उनके भाई लक्ष्मणने आध्यात्मिक ज्ञानकी चर्चा तदनन्तर श्रीराम तथा लक्ष्मणसे शूर्पणखाकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14329)
- **Original**: करके उन्हें सचेत किया। -..... “था लक्ष्मणसे शूर्पणखाकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14330)
- **Original**: करके उन्हें सचेत किया। मुने। तत्पश्षात्‌ वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14331)
- **Original**: तत्पश्चात्‌ वे * न हि सत्यात्‌ परो धर्मों नानृतात्‌ पातकं परम्‌ ।न हि गज्जासम॑ तीथ॑ न देव: केशवातू पर:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14332)
- **Original**: जास्ति धर्मात्‌ परो बन्धुर्ास्ति धर्मात्‌ पर॑ धनम्‌ । धर्मात्‌ प्रियः पर: को वा स्वधर्म रक्ष यत्रत:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14333)
- **Original**: स्वधर्म रक्षिते तात शश्वत्‌ सर्वत्र मज़लम्‌ । यशस्यं सुप्रतिष्ठा च प्रताप: पूजन॑ परम्‌
- **Translation**: 

---

