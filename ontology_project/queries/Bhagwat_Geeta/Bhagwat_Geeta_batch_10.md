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

### Verse 1 (Bhagwat_Geeta 2.181)
- **Original**: * अध्याय 2* 29 न त्वेवाहं जातु नासं न त्वं नेमे जनाधिपा: । न चैव न भविष्याम:ः सर्वे वयमतः परम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 2.182)
- **Original**: न तो ऐसा ही है कि मैं किसी कालमें नहीं था, तू नहीं था अथवा ये राजालोग नहीं थे और न ऐसा ही है कि इससे आगे हम सब नहीं रहेंगे
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 2.183)
- **Original**: देहिनो5स्मिन्यथा देहे कौमारं यौवनं जरा। तथा उदेहान्तरप्राप्तिर्धीरस्तत्र न मुहायति
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 2.184)
- **Original**: जैसे जीवात्माकी इस देहमें बालकपन, जवानी और वृद्धावस्था होती है, वैसे ही अन्य शरीरकी प्राप्ति होती है; उस विषयमें धीर पुरुष मोहित नहीं होता
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 2.185)
- **Original**: मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदुःखदा: । आगमापायिनो_नित्यास्तांस्तितिक्षस्त्र भारत
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 2.186)
- **Original**: हे कुन्तीपुत्र! सर्दी-गर्मी और सुख-दुःखको देनेवाले इन्द्रिय और विषयोंके संयोग तो उत्पत्ति- विनाशशील और अनित्य हैं, इसलिये हे भारत! उनको तू सहन कर
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 2.187)
- **Original**: य॑ हि न व्यथयन्त्येते पुरुषं पुरुषर्षभ। समदुःखसुखं धीरं सो5मृतत्वाय कल्पते
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 2.188)
- **Original**: क्योंकि हे पुरुषश्रेष्ठ! दुःख-सुखको समान
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 2.189)
- **Original**: 30 * श्रीमद्धगवद्रीता * समझनेवाले जिस धीर पुरुषको ये इन्द्रिय और विषयोंके संयोग व्याकुल नहीं करते, वह मोक्षके योग्य होता है
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 2.190)
- **Original**: नासतो विद्यते भावो नाभावो विद्यते सतः। उभयोरपि दृष्टो5न्तस्त्वनयोस्तत्त्वदर्शिभि:
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 2.191)
- **Original**: असत्‌ वस्तुकी तो सत्ता नहीं है और सत्‌का अभाव नहीं है। इस प्रकार इन दोनोंका ही तत्त्व तत्त्वज्ञानी पुरुषोंद्रारा देखा गया है
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 2.192)
- **Original**: अविनाशि तु तद्विद्द्धि येन सर्वमिदं ततम्‌। विनाशमव्ययस्यास्थ न कश्रित्कर्तुमईति
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 2.193)
- **Original**: नाशरहित तो तू उसको जान, जिससे यह सम्पूर्ण जगत्‌-दृश्यवर्ग व्याप्त है । इस अविनाशीका विनाश करनेमें कोई भी समर्थ नहीं है
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 2.194)
- **Original**: अन्तवन्त इमे देहा नित्यस्योक्ता: शरीरिण: । अनाशिनो5प्रमेयस्य तस्माद्युध्यस्व भारत
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 2.195)
- **Original**: इस नाशरहित, अप्रमेय, नित्यस्वरूप जीवात्माके ये सब शरीर नाशवानू कहे गये हैं। इसलिये हे भरतवंशी अर्जुन! तू युद्ध कर
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 2.196)
- **Original**: य एन वेत्ति हन्तारं यश्लेनं मन्‍्यते हतम्‌। उभौ तौ न विजानीतो नाय॑ हन्ति न हन्यते
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 2.197)
- **Original**: जो इस आत्माको मारनेवाला समझता है तथा
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 2.198)
- **Original**: * अध्याय 2* 391 जो इसको मरा मानता है, वे दोनों ही नहीं जानते; क्योंकि यह आत्मा वास्तवमें न तो किसीको मारता है और न किसीके द्वारा मारा जाता है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 2.199)
- **Original**: न जायते प्रियते वा कदाचि- न्ञाय॑ भूत्वा भविता वा न भूयः । अआजो नित्य: शाश्रतो<5यं पुराणो- न हन्यते हन्यमाने शारीरे
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 2.200)
- **Original**: यह आत्मा किसी कालमें भी न तो जन्मता है और न मरता ही है तथा न यह उत्पन्न होकर फिर होनेवाला ही है; क्योंकि यह अजन्मा, नित्य, सनातन और पुरातन है; शरीरके मारे जानेपर भी यह नहीं मारा जाता
- **Translation**: 

---

