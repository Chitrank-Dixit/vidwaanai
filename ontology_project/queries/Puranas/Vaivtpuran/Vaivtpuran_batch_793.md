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

### Verse 1 (Vaivtpuran 543.14174)
- **Original**: अपने ब्रह्मनिष्ठ गुरु कृपानिधान बृहस्पतिकी स्तुति वह आजीबन देबता, पितर और ब्राह्मणकी पूजाके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14175)
- **Original**: करने लगी। लिये अपना अधिकार खो बैठता है, मनुष्यतासे।_ शची बोली--महाभाग! मैं भयभीत हो गिर जाता है तथा कलझ्लित हो जाता है। जो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14176)
- **Original**: आपकी शरणमें आयी हूँ। आप ईश्वर हैं और तीसरे दिन रजस्वला पत्नौके साथ समागम करता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14177)
- **Original**: मैं शोकसागरमें डूबी हुई आपकी दासी हूँ। आप है, वह मूढ़ भ्रूण-हत्याका भागी होता है; इसमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14178)
- **Original**: मेरी रक्षा कीजिये, रक्षा कौजिये। गुरु असमर्थ संशय नहीं है। पहले बताये हुए लोगोंकी भाँति हो या समर्थ, बलवान्‌ हो या निर्बल, वह अपने वह भी पतित होकर सम्पूर्ण कमॉंका अनधिकारी शिष्यों, पत्नी तथा पुत्रॉपर सदा शासन करनेपें हो जाता है। चौथे दिन रजस्वला असत्‌ शुद्रा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14179)
- **Original**: समर्थ है। प्रभो! आपने अपने शिष्यको उसके कही जाती है; अतः विद्वान्‌ पुरुष उस दिन भी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14180)
- **Original**: राज्यसे दूर कर दिया। बहुत दिन हुए, अब तो उसके पास न जाय। मूढ़! मैं तेरी माता हूँ!
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14181)
- **Original**: उसके दोषकी शान्ति हो गयी होगी। अतः कृपा यदि तू माताकों भी बलपूर्वक ग्रहण करना चाहता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14182)
- **Original**: कीजिये। कृपानिधे! मैं अनाथ हूँ। मेरे लिये सब है तो आज छोड़ दे। ऋतुकाल बीत जानेपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14183)
- **Original**: दिशाएँ सूनी हो गयी हैं। अमरावतीपुरी भी सूनी जैसी तेरी मर्जी हो, करना।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14184)
- **Original**: है तथा मेरा निवासस्थान भी सब प्रकारकी इतनेपर भी नहुष नहीं माना और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14185)
- **Original**: सम्पत्तियोंसे शून्य है। मेरी इस अवस्थापर बोला--' देवरमणी सदा हो शुद्ध होती है। तुम दृष्टिपात कौजिये और मुझे संकटसे बचाइये। मुझे अपने घर चलो। मैं अभी आता हूँ '--यों कहकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14186)
- **Original**: एक डाकू अपना ग्रास बनाना चाहता है। आप राजा नहुष प्रसन्नतापूर्वक रत्रमय रथपर आरूढ़
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14187)
- **Original**: मेरी रक्षा कीजिये। अपने किड्भूर देवराजको यहाँ हो नन्दनवनमें शचीके भवनकी ओर गया; परंतु
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14188)
- **Original**: ले आइये। चरणोंकी धूल देकर उन्हें शुभाशीर्वादसे शी अपने घरमें नहीं लौटी। वह सीधे गुरु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14189)
- **Original**: अनुगृहीत कीजिये। वृहस्पतिके घर चली गयी। वहाँ जाकर उसने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14190)
- **Original**: समस्त गुरुओमें जन्मदाता पिता श्रेष्ठ गुरु देखा गुरुदेव कुशासनपर विराजमान हैं। तारादेवी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14191)
- **Original**: माने गये हैं। पिताकी अपेक्षा माता सौगुनी अधिक उनके चरणारविन्दोंकी सेवा कर रही हैं। वे पूजनीया, वन्दनीया तथा वरिष्ठ है; परंतु जो ब्रह्मतेजसे प्रकाशमान हैं और हाथमें जपमाला
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14192)
- **Original**: विद्यादाता, मन्त्रदाता, ज्ञानदाता और हरिभक्ति लिये अपने अभीष्ट देव श्रीकृष्णके नामका निरन्तर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14193)
- **Original**: प्रदान करनेवाले गुरु हैं, वे मातासे भी सौगुने जप कर रहे हैं। वे श्रीकृष्ण सबसे उत्कृष्ट, पूजनीय, वन्दगीय और सेव्य हैं। जिन्होंने
- **Translation**: 

---

